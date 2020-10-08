from django.shortcuts import render

# 광현's part
def setting(request):
    return render(request, 'settingapp/setting.html') 

def sales(request):
    return render(request, 'settingapp/sales.html')

def settingmenu(request):
    return render(request, 'settingapp/settingmenu.html')

def addmenu(request):
    return render(request, 'settingapp/addmenu.html')

def editmenu(request):
    return render(request, 'settingapp/editmenu.html')

def optionlist(request):
    return render(request, 'settingapp/optionlist.html')