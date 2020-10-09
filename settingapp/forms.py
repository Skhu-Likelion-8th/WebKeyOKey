from django import forms
from main.models import Menu, Option

class AddForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['m_name', 'm_info', 'm_price', 'm_img']

class EditForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['m_name', 'm_info', 'm_price', 'm_img']

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['option_name', 'option_price']