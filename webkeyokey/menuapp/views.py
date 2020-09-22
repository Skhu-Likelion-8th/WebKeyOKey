from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request, 'menuapp/menu.html')

def optionmenu(request):
    return render(request, 'menuapp/optionmenu.html')

def checkmenu(request):
    return render(request, 'menuapp/checkmenu.html')

def pay(request):
    return render(request, 'menuapp/pay.html')

def success(request):
    return render(request, 'menuapp/success.html')