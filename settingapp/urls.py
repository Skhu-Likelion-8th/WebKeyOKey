from django.urls import path, include
from settingapp import views

urlpatterns = [
    path('', views.setting, name='setting'),
    path('sales/', views.sales, name='sales'),
    path('settingmenu/', views.settingmenu, name='settingmenu'),
    path('addmenu/', views.addmenu, name='addmenu'),
    path('editmenu/', views.editmenu, name='editmenu'),
    path('optionlist/', views.optionlist, name='optionlist'),
]