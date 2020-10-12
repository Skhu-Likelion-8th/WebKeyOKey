from django import forms
from .models import CustomUser
#from django.contrib.auth.models import User

class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        # fields = ['u_id', 'password']
        fields = ['username', 'password']