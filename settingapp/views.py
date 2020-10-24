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

# 달력구현
import datetime
import calendar
from .calendar import Calendar
from django.utils.safestring import mark_safe

def sales(request):
    today = get_date(request.GET.get('month'))

    prev_month_var = prev_month(today)
    next_month_var = next_month(today)

    cal = Calendar(today.year, today.month)
    html_cal = cal.formatmonth(withyear=True)
    result_cal = mark_safe(html_cal)

    context = {'calendar' : result_cal, 'prev_month' : prev_month_var, 'next_month' : next_month_var}

    return render(request, 'settingapp/sales.html', context)

#현재 달력을 보고 있는 시점의 시간을 반환
def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return datetime.date(year, month, day=1)
    return datetime.datetime.today()

#현재 달력의 이전 달 URL 반환
def prev_month(day):
    first = day.replace(day=1)
    prev_month = first - datetime.timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

#현재 달력의 다음 달 URL 반환
def next_month(day):
    days_in_month = calendar.monthrange(day.year, day.month)[1]
    last = day.replace(day=days_in_month)
    next_month = last + datetime.timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
