from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm
from .models import Category,Course, Profile
from .models import Chat

# Create your views here.
def index(request):
    courses = Course.objects.all()

    return render(request, 'index.html', {
        'courses': courses
    })

def signup_view(request, role):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            user = User.objects.create_user(username=username, email=email, password=password)
            return redirect('login', role=role)

    return render(request, 'signup.html', {'role': role})

def login_view(request, role):
    next_url = request.GET.get('next') or request.POST.get('next') or '/'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in!')

            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html', {'role': role})

def logout_view(request):
    logout(request)
    return redirect('index')

# @login_required
def purchased_courses(request):
    courses = Course.objects.all()

    if request.user.is_authenticated:   
        is_student = request.user.profile.is_student()
        is_tutor = request.user.profile.is_tutor()
    else:
        is_student = False
        is_tutor = False
    
    return render(request, 'purchased_courses.html', {
        'courses': courses,  
        'is_student': is_student,
        'is_tutor': is_tutor
    })

def categories(request):

    categories = Category.objects.all()


    if request.user.is_authenticated:
        is_student = request.user.profile.is_student()
        is_tutor = request.user.profile.is_tutor()
    else:
        is_student = False
        is_tutor = False
    
    return render (request, 'categories.html', {
        'categories': categories,
        'is_student': is_student,
        'is_tutor': is_tutor
    })

def create_courses(request):
    return render(request, 'create_courses.html')

def uploaded_courses(request):
    return render(request, 'uploaded_courses.html')

def technology(request):
    return render(request, 'technology.html')


def course_title(request):
    return render(request, 'course_title.html')

def chat(request):  
    chats = Chat.objects.all()  

    if request.user.is_authenticated:
        is_student = request.user.profile.is_student()  
        is_tutor = request.user.profile.is_tutor()    
    else:
        is_student = False
        is_tutor = False

    return render(request, 'chat.html', {
        'chats': chats,       
        'is_student': is_student,
        'is_tutor': is_tutor,
    })  
def profile(request):
    
    profiles = Profile.objects.all()

    if request.user.is_authenticated:
        is_student = request.user.profile.is_student()
        is_tutor = request.user.profile.is_tutor()
    else:
        is_student = False
        is_tutor = False
    
    return render(request, 'profile.html', {
        'profiles': profiles,
        'is_student': is_student,
        'is_tutor': is_tutor
    })