from .models import OrderReview, Profile, Order, OrderLine
from django import forms
from django.contrib.auth.models import User


class OrderReviewForm(forms.ModelForm):
    class Meta:
        model = OrderReview
        fields = ('content', 'order_id', 'reviewer',)
        widgets = {'order_id': forms.HiddenInput(), 'reviewer': forms.HiddenInput()}


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']


class DateInput(forms.DateInput):
    input_type = 'date'


class UserOrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['date', 'auto_id', 'due_back']
        widgets = {'due_back': DateInput(), 'date': DateInput()}


class UserOrderLineCreateForm(forms.ModelForm):
    class Meta:
        model = OrderLine
        fields = ['service_id', 'amount', 'order_id']
