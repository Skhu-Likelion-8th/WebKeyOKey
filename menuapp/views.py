from django.shortcuts import render, redirect, get_object_or_404
from main.models import CustomUser, Menu, Option, Basket, Pay
from datetime import datetime
from django.utils.dateformat import DateFormat
import random

# Create your views here.
def menu(request):
    menus = Menu.objects.all()
    return render(request, 'menuapp/menu.html', {'menus':menus})

def optionmenu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    basket = Basket()
    if request.method == 'POST':
        basket.menu_id = menu
        basket.takeout = False
        if request.POST.getlist('takeout') != []:
            basket.takeout = True
        basket.count = request.POST['count']
        basket.ototal_price = menu.m_price
        check_values = request.POST.getlist('option[]')
        op_list = list()
        for c in check_values:
            if Option.objects.filter(option_name=c).exists():
                op = Option.objects.get(option_name=c)
                basket.ototal_price += op.option_price
                op_list.append(op)

        basket.ototal_price *= int(basket.count)
        basket.save()
        basket.b_options.add(*op_list)
    return render(request, 'menuapp/optionmenu.html', {'menu':menu})

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