from django import forms
from main.models import CustomUser
#from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'u_id', 'password', 'email', 'phone', 'question_id', 'answer']