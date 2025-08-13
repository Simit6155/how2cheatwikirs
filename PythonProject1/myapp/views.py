from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'myapp/login.html', {'error': 'Invalid credentials'})

    return render(request, 'myapp/login.html')


@login_required
def index(request):
    return render(request, 'myapp/index.html', {'user': request.user})


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'myapp/register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'myapp/register.html', {'error': 'Username already taken'})

        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Account created! You can now log in.')
        return redirect('login')

    return render(request, 'myapp/register.html')


def home_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    return redirect('login')


@login_required
def roblox_view(request):
    return render(request, 'myapp/roblox.html')


@login_required
def minecraft_view(request):
    return render(request, 'myapp/minecraft.html')


def offline_view(request):
    return render(request, 'myapp/offline.html')
