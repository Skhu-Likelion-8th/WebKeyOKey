from django.urls import path, include
from settingapp import views

urlpatterns = [
    path('', views.setting, name='setting'),
    path('bye/', views.bye, name='bye'),
    path('delete/<int:pk>', views.delete, name='delete'), #글 삭제하는 것
    path('option/', views.option, name='option'),
    path('sales/', views.sales, name='sales'),
    path('settingmenu/', views.settingmenu, name='settingmenu'),
    path('addmenu/', views.addmenu, name='addmenu'),
    path('editmenu/<int:pk>', views.editmenu, name='editmenu'),
    path('delete_user/<int:pk>', views.delete, name='delete_user'), #유저 삭제하는 것
    path('optionlist/', views.optionlist, name='optionlist'),
]