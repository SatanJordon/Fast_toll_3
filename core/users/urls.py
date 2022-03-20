from django.urls import path, include
from . import views as v

urlpatterns = [
    path('accounts/register/', v.register, name='register'),
    path('', v.index, name='index'),
    path('accounts/profile/', v.profile, name='profile'),
]
