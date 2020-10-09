from django.shortcuts import render, redirect, get_object_or_404
from main.models import Menu
from .forms import AddForm, EditForm

# 광현's part, 찬미's part
def setting(request):
    return render(request, 'settingapp/setting.html') 

def sales(request):
    return render(request, 'settingapp/sales.html')

def settingmenu(request):
    menus = Menu.objects.all
    return render(request, 'settingapp/settingmenu.html', {'menus': menus})

def addmenu(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('settingapp/addmenu')
    else:
        form = AddForm()
        return render(request, 'settingapp/addmenu.html', {'form':form})

def editmenu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        form = EditForm(request.POST, instance=menu)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('settingmenu')
    else:
        form = EditForm(instance=menu)
        return render(request, 'settingapp/editmenu.html', {'form':form})

def delete(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    menu.delete()
    return redirect('settingmenu')

def optionlist(request):
    return render(request, 'settingapp/optionlist.html')

def bye(request):
    return render(request, 'settingapp/bye.html')

def option(request):
    return render(request, 'settingapp/option.html')