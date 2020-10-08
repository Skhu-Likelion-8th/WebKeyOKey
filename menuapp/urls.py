from django.urls import path, include
from menuapp import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('optionmenu/<int:pk>', views.optionmenu, name='optionmenu'),
    path('checkmenu/', views.checkmenu, name='checkmenu'),
    path('checkmenu/delete/<int:pk>', views.delete, name='delete'),
    path('pay/', views.pay, name='pay'),
    path('pay/success/<int:pk>', views.success, name='success'),
    # 광현's part
    path('order/',views.order, name='order'),
    path('orderdetail/',views.orderdetail, name='orderdetail'),
]