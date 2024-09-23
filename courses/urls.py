from django.urls import path
from . import views
import courses

# http://127.0.0.1:8000/
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('studentsignup', views.studentsignup, name='studentsignup'),
    path('instructorsignup', views.instructorsignup, name='instructorsignup'),
    path('login/', views.login_view, name='login'),
    path('studentlogin', views.studentlogin, name='studentlogin'),
    path('instructorlogin', views.instructorlogin, name='instructorlogin'),
    path('logout/', views.logout_view, name='logout'),
    path('categories', views.categories, name='categories'),
    path('instructor_homepage', views.instructor_homepage , name='instructor_homepage'),
    path('student_categories', views.student_categories , name='student_categories'),
    path('instructor_categories', views.instructor_categories , name='instructor_categories'),
    path('/purchased_courses/', views.purchased_courses , name='purchased_courses'),
    path('student_purchasedcourses/', views.student_purchasedcourses, name='student_purchasedcourses'),
    path('instructor_purchased_courses', views.instructor_purchased_courses , name='instructor_purchased_courses'),  
    path('uploaded_courses', views.uploaded_courses , name='uploaded_courses'), 
    path('create_courses', views.create_courses, name='create_courses'),
    path('instructor_profile', views.instructor_profile, name='instructor_profile'),
    
    
]
