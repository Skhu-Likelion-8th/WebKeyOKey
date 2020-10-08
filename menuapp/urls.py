from django.urls import path, include
from menuapp import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('optionmenu/', views.optionmenu, name='optionmenu'),
    path('checkmenu/', views.checkmenu, name='checkmenu'),
    path('pay/', views.pay, name='pay'),
    path('success/', views.success, name='success'),
    # 광현's part
    path('order/',views.order, name='order'),
    path('orderdetail/',views.orderdetail, name='orderdetail'),
]