from django.shortcuts import render, redirect, get_object_or_404
from main.models import CustomUser, Menu, Option, Basket, Pay
from datetime import datetime
from django.utils.dateformat import DateFormat
import random

# Create your views here.
def menu(request):
    menus = Menu.objects.all()
    return render(request, 'menuapp/menu.html', {'menus':menus})

def optionmenu(request):
    return render(request, 'menuapp/optionmenu.html')

def checkmenu(request):
    baskets = Basket.objects.all()
    return render(request, 'menuapp/checkmenu.html', {'baskets': baskets})
def delete(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.delete()
    return redirect('checkmenu')

def pay(request):
    return render(request, 'menuapp/pay.html')

def success(request):
    return render(request, 'menuapp/success.html')

# 광현's part
def order(request):
    return render(request, 'menuapp/order.html')

def orderdetail(request):
    return render(request, 'menuapp/orderdetail.html')