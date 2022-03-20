from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import Account


class CustomUserLoginForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1')


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class CustomAccountCreationForm(ModelForm):
    class Meta:
        model = Account
        fields = ('car_number', 'gender')
