from django.urls import path
from . import views
import courses

# http://127.0.0.1:8000/
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login/<str:role>/', views.login_view, name='login'), 
    path('signup/<str:role>/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('categories', views.categories, name='categories'),
    path('purchased_courses/', views.purchased_courses , name='purchased_courses'),
    path('uploaded_courses/', views.uploaded_courses , name='uploaded_courses'), 
    path('create_courses/', views.create_courses, name='create_courses'),
    path('profile', views.profile, name='profile'),
    path('technology', views.technology, name='technology'),
    path('course_title', views.course_title, name='course_title'),
    path('chat', views.chat, name='chat'),
]
