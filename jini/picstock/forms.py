from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput,PasswordInput

##
class PicStockForm(forms.ModelForm):
    class Meta:
        model = PicStock
        fields = ['name','image']


##RegisterUserForm
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","password1","password2"]

# --Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
