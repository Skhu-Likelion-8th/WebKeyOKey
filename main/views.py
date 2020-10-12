from django.shortcuts import render, redirect, get_object_or_404
from .models import CustomUser
from .forms import SigninForm

#from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.
def home(request):
    signin_form = SigninForm()
    return render(request, 'main/home.html', {'signin_form': signin_form})

from django.contrib import messages
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        # u_id = request.POST['u_id']
        password = request.POST['password']
        # user = authenticate(u_id = u_id, password = password)
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request,'username or password not correct')
            return redirect('home')


def boss(request):
    return render(request, 'main/boss.html')