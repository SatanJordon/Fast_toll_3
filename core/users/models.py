from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.forms import ModelForm


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    car_number = models.CharField(max_length=200, blank=False)
    gender = models.CharField(max_length=6, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')])

    def __str__(self):
        return self.user.username


class Tax(models.Model):
    t_car_number = models.CharField(max_length=200, blank=False)
    time = models.CharField(max_length=300)
    is_registered = models.CharField(max_length=6)
    amount = models.CharField(max_length=1000)

