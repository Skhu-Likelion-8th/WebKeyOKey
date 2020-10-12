from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import views
from .forms import UserForm
from main.models import CustomUser

from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# from django.contrib.auth.forms import PasswordChangeForm
# from django.contrib.auth import update_session_auth_hash

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = CustomUser.objects.create_user(username=form.cleaned_data['username'],
            u_id=form.cleaned_data['u_id'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'],
            phone=form.cleaned_data['phone'],
            question_id=form.cleaned_data['question_id'],
            answer=form.cleaned_data['answer'])
            login(request, new_user)
            return redirect('home')
    else:
        form = UserForm()
        return render(request, 'userapp/signup.html', {'form': form})

#1.보안문제 풀기 2. 임시저장
# 아이디 먼저 확인 -> 유저 정보 확인 -> 1) 아이디 없음 2) 메일보내기

# def password(request):
#     if not request.user.is_active:
#         return HttpResponse('First Signin Please')

#     if request.method == 'POST':
#         password_change_form = PasswordChangeForm(request.user, request.POST)

#         if password_change_form.is_valid():
#             user = password_change_form.save()
#             update_session_auth_hash(request, user)
#             return redirect('userapp/password.html', request.user.username)
    
#     else:
#         password_change_form = PasswordChangeForm(request.user)
#     return render(request, 'userapp/password.html', { 'password_change_form' : password_change_form})
