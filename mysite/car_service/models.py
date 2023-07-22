from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime
from tinymce.models import HTMLField
from PIL import Image
from django.utils.translation import gettext_lazy as _


class CarModel(models.Model):
    make = models.CharField(_('make'), max_length=20, null=True, blank=True)
    model = models.CharField(_('model'), max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.make} '{self.model}'"

    class Meta:
        verbose_name = "Car model"
        verbose_name_plural = "Car models"


class Auto(models.Model):
    plate_number = models.CharField(_('plate_number'), max_length=20, null=True, blank=True)
    car_model_id = models.ForeignKey('CarModel', on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='clientauto')
    vin_code = models.CharField('VIN_code', max_length=20, null=True, blank=True)
    client = models.CharField(_('clieant'), max_length=20, null=True, blank=True)
    description = HTMLField()
    cover = models.ImageField(_('Photo'), upload_to='covers', null=True, blank=True)

    def __str__(self):
        return f"{self.car_model_id.make} '{self.car_model_id.model}' '{self.plate_number}' | {self.client}"

    class Meta:
        verbose_name = "Client auto"
        verbose_name_plural = "Client autos"


class Order(models.Model):
    date = models.DateTimeField(_('date'), default=datetime.today(), null=True, blank=True)
    auto_id = models.ForeignKey('Auto', on_delete=models.SET_NULL, null=True, blank=True)
    total_price = models.FloatField(_('total_price'), default=0)
    client_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='user')
    due_back = models.DateField(_('due_back'), null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    ORDER_STATUS = (
        ('a', 'Accepted'),
        ('p', 'In progress'),
        ('c', 'Completed'),
    )

    status = models.CharField(max_length=1, choices=ORDER_STATUS, blank=True, null=True, default='a',
                              help_text='Order status',
                              )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return f'(Order ID): {self.id} (Date): {self.date} '


class Service(models.Model):
    name = models.CharField(_('name'), max_length=20, null=True, blank=True)
    price = models.FloatField(_('price'), default=0, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.price} EUR)'

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class OrderLine(models.Model):
    service_id = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True, blank=True)
    order_id = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField(_('amount'), null=True, blank=True)

    # sum = models.FloatField(_('sum'), default=0, null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     order_lines = OrderLine.objects.filter(id=self.id)
    #     self.sum = 0
    #     for order_line in order_lines:
    #         self.sum += order_line.amount * order_line.service_id.price
    #     super().save(*args, **kwargs)

    @property
    def sum(self):
        order_lines = OrderLine.objects.filter(id=self.id)
        sum = 0
        for order_line in order_lines:
            sum += order_line.amount * order_line.service_id.price
        return sum

    ####PVZ
    # class MyModel(models.Model):
    #     field1 = models.IntegerField()
    #     field2 = models.IntegerField()
    #     total = models.IntegerField(editable=False, null=True)
    #
    #     def save(self, *args, **kwargs):
    #         self.total = self.field1 + self.field2
    #         super().save(*args, **kwargs)

    def __str__(self):
        return f'(Order ID): {self.order_id.id} (Order line ID): {self.id}'

    class Meta:
        verbose_name = "Order line"
        verbose_name_plural = "Order lines"


class OrderReview(models.Model):
    order_id = models.ForeignKey('Order', on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    content = models.TextField(_('review'), max_length=2000, null=True, blank=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = 'Reviews'
        ordering = ['-date_created']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(default="img/no-image.jpg", upload_to="profile_pics", null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.photo.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
