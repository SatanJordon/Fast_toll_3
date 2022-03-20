from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm, CustomAccountCreationForm
from .models import Account, Tax


def index(response):
    return render(response, 'users/home.html')


@login_required
def profile(response):
    user = response.user
    account = Account.objects.get(user=user)
    tax = Tax.objects.get(t_car_number=account.car_number)

    context = {
        'name': user.first_name,
        'email': user.email,
        'amount': tax.amount,
        'car_number': account.car_number
    }
    return render(response, 'users/profile.html', context)


def register(response):
    if response.method == 'POST':
        user = CustomUserCreationForm(response.POST)
        account = CustomAccountCreationForm(response.POST)
        if user.is_valid() and account.is_valid():
            user_form = user.save()
            account_form = account.save(commit=False)
            account_form.user = user_form
            account_form.save()
            return redirect('/')
    else:
        user = CustomUserCreationForm()
        account = CustomAccountCreationForm()

    return render(response, "users/register.html", {"user": user, "account": account})
