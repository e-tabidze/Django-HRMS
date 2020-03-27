from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django .contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_login(request):
    if request.method == "POST":
        user = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)
            redirect('/employees')
    context = {}
    return render(request, 'login.html', context)


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for' + user)
            return redirect('/login')
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)



