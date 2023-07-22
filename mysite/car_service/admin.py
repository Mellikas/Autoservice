from django.contrib import admin
from .models import CarModel, Auto, Order, Service, OrderLine, OrderReview, Profile


class OrderLineInline(admin.TabularInline):
    model = OrderLine
    readonly_fields = ('id','sum')
    can_delete = False
    extra = 0  # išjungia papildomas tuščias eilutes įvedimui


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'auto_id', 'total_price', 'status', 'date')
    inlines = [OrderLineInline]
    fieldsets = (
        (None, {'fields': ('auto_id', 'client_user', 'due_back', 'status')}),
    )


class AutoAdmin(admin.ModelAdmin):
    list_display = ('client', 'plate_number', 'car_model_id', 'vin_code')
    list_filter = ('car_model_id', 'client')
    search_fields = ['plate_number', 'vin_code']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


class OrderReviewAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'date_created', 'reviewer', 'content')


admin.site.register(CarModel)
admin.site.register(Auto, AutoAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(OrderLine)
admin.site.register(OrderReview, OrderReviewAdmin)
admin.site.register(Profile)