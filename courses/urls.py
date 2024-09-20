from django.urls import path
from . import views
import courses

# http://127.0.0.1:8000/
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('categories', views.categories, name='categories'),
    path('purchased_courses', views.purchased_courses , name='purchased_courses'),
    path('student_homepage', views.student_homepage , name='student_homepage'),
    path('student_categories', views.student_categories , name='student_categories'),
    path('student_purchasedcourses', views.student_purchasedcourses , name='student_purchasedcourses'),
    path('instructor_homepage', views.instructor_homepage , name='instructor_homepage'),
    path('instructor_categories', views.instructor_categories , name='instructor_categories'),
    path('instructor_purchased_courses', views.instructor_purchased_courses , name='instructor_purchased_courses'),  
    path('uploaded_courses', views.uploaded_courses , name='uploaded_courses'), 
    path('studentlogin', views.studentlogin, name='studentlogin'),
    path('studentsignup', views.studentsignup, name='studentsignup'),
    path('instructorlogin', views.instructorlogin, name='instructorlogin'),
    path('instructorsignup', views.instructorsignup, name='instructorsignup'),
    path('create_courses', views.create_courses, name='create_courses'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
