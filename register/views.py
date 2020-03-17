from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm


def register(response):
    form = UserCreationForm()
    return render(response, 'register/register.html', {"form": form})