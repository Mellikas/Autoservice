from .models import Auto, CarModel, OrderLine, Order, Service
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from .forms import OrderReviewForm, UserUpdateForm, ProfileUpdateForm, UserOrderCreateForm, UserOrderLineCreateForm
from django.views.generic.edit import FormMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.utils.translation import gettext as _


def index(request):
    # paslaugų kiekis, automobilių kiekis, atliktų užsakymų kiekis
    count_services = Service.objects.all().count()
    count_client_autos = Auto.objects.all().count()
    count_completed_orders = Order.objects.filter(status__exact='c').count()
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'count_services': count_services,
        'count_client_autos': count_client_autos,
        'count_completed_orders': count_completed_orders,
        'num_visits': num_visits,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'index.html', context=context)


def autos(request):
    paginator = Paginator(Auto.objects.all(), 3)
    page_number = request.GET.get('page')
    autos = paginator.get_page(page_number)
    context = {
        'autos': autos
    }
    return render(request, 'autos.html', context=context)


def clientauto(request, clientauto_id):
    single_auto = get_object_or_404(Auto, pk=clientauto_id)
    return render(request, 'clientauto.html', {'clientauto': single_auto})


class OrderListView(generic.ListView):
    model = Order
    paginate_by = 2
    template_name = 'order_list.html'


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'order_detail.html'


def search(request):
    query = request.GET.get('query')
    search_results = Auto.objects.filter(
        Q(client__icontains=query) |
        Q(plate_number__icontains=query) |
        Q(vin_code__icontains=query) |
        Q(car_model_id__model__icontains=query) |
        Q(car_model_id__make__icontains=query)
    )
    context = {'autos': search_results, 'query': query}
    return render(request, template_name='search.html', context=context)


class ClientOrdersByUserListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'user_orders.html'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(client_user=self.request.user).order_by('due_back')


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, _('Username %s already exists!') % username)
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request,  _('Email %s already exists!') % email)
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'User {username} resgistered successfully!')
                    return redirect('login')
        else:
            messages.error(request, _('Passwords do not match!'))
            return redirect('register')
    return render(request, 'register.html')


class OrderDetailView(FormMixin, generic.DetailView):
    model = Order
    template_name = 'order_detail.html'
    form_class = OrderReviewForm

    # nurodome, kur atsidursime komentaro sėkmės atveju.
    def get_success_url(self):
        return reverse('order_detail', kwargs={'pk': self.object.id})

    # standartinis post metodo perrašymas, naudojant FormMixin, galite kopijuoti tiesiai į savo projektą.
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # štai čia nurodome, kad knyga bus būtent ta, po kuria komentuojame, o vartotojas bus tas, kuris yra prisijungęs.
    def form_valid(self, form):
        form.instance.order_id = self.object
        form.instance.reviewer = self.request.user
        form.save()
        return super(OrderDetailView, self).form_valid(form)


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Profile updated")
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)


class OrderByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = Order
    success_url = "/car_service/myorders/"
    template_name = 'user_order_form.html'
    form_class = UserOrderCreateForm

    def form_valid(self, form):
        form.instance.client_user = self.request.user
        return super().form_valid(form)


class OrderByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Order
    fields = ['id', 'auto_id', 'due_back']
    success_url = "/car_service/myorders/"
    template_name = 'user_order_form.html'

    def form_valid(self, form):
        form.instance.client_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.client_user


class OrderByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Order
    success_url = "/car_service/myorders/"
    template_name = 'user_order_delete.html'

    def test_func(self):
        order = self.get_object()
        return self.request.user == order.client_user


class OrderLineByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = OrderLine
    # fields = ['service_id', 'amount']
    success_url = "/car_service/myorders/"
    template_name = 'user_order_detail_form.html'
    form_class = UserOrderLineCreateForm

    def form_valid(self, form):
        form.instance.order_id.client_user = self.request.user
        return super().form_valid(form)


class OrderLineByUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = OrderLine
    fields = ['service_id', 'amount']
    success_url = "/car_service/myorders/"
    template_name = 'user_order_detail_form.html'

    def form_valid(self, form):
        form.instance.order_id.client_user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        order_line = self.get_object()
        return self.request.user == order_line.order_id.client_user


class OrderLineByUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = OrderLine
    success_url = "/car_service/myorders/"
    template_name = 'user_order_detail_delete.html'


    def test_func(self):
        order_line = self.get_object()
        return self.request.user == order_line.order_id.client_user