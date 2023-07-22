from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autos/', views.autos, name='autos'),
    path('autos/<int:clientauto_id>', views.clientauto, name='clientauto'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('myorders/', views.ClientOrdersByUserListView.as_view(), name='my_order'),
    path('myorders/new', views.OrderByUserCreateView.as_view(), name='my_order_new'),
    path('myorders/<int:pk>/update', views.OrderByUserUpdateView.as_view(), name='my_order_update'),
    path('myorders/<int:pk>/delete', views.OrderByUserDeleteView.as_view(), name='my_order_delete'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('orders/new', views.OrderLineByUserCreateView.as_view(), name='my_order_line_new'),
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name='order_detail'),
    path('orders/<int:pk>/update', views.OrderLineByUserUpdateView.as_view(), name='my_order_line_update'),
    path('orders/<int:pk>/delete', views.OrderLineByUserDeleteView.as_view(), name='my_order_line_delete'),
    path('i18n/', include('django.conf.urls.i18n')),
]

