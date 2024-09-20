from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from .models import Course

# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

def index(request):
    return render(request, 'index.html')

def purchased_courses (request):
    return render(request, 'purchased_courses.html')

def studentlogin(request):
    return render(request, 'studentlogin.html')

def categories(request):
    return render(request, 'categories.html')

def instructorlogin(request):
    return render(request, 'instructorlogin.html')

def instructorsignup(request):
    return render(request, 'instructorsignup.html')

def student_homepage(request):
    return render(request, 'student_homepage.html')

def student_categories(request):
    return render(request, 'student_categories.html')

def student_purchasedcourses(request):
    return render(request, 'student_purchasedcourses.html')

def instructor_homepage(request):
    return render(request, 'instructor_homepage.html')

def instructor_categories(request):
    return render(request, 'instructor_categories.html')

def instructor_purchased_courses(request):
    return render(request, 'instructor_purchased_courses.html')

def create_courses(request):
    return render(request, 'create_courses.html')

def uploaded_courses(request):
    return render(request, 'uploaded_courses.html')

def studentsignup(request):
    return render(request, 'studentsignup.html')


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
