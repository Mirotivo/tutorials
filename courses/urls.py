from django.urls import path
from . import views

# http://127.0.0.1:8000/
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('studentsignup/', views.studentsignup, name='studentsignup'),
    path('instructorsignup/', views.instructorsignup, name='instructorsignup'),
    path('login/', views.login_view, name='login'),
    path('studentlogin/', views.studentlogin, name='studentlogin'),
    path('instructorlogin/', views.instructorlogin, name='instructorlogin'),
    path('logout/', views.logout_view, name='logout'),
    path('categories/', views.categories, name='categories'),
    path('purchased_courses/', views.purchased_courses, name='purchased_courses'),
]
