from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from .models import Course

# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def studentlogin(request):
    return render(request, 'studentlogin.html')

def categories(request):
    return render(request, 'categories.html')

def instructorlogin(request):
    return render(request, 'instructorlogin.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
