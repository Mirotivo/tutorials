from django.urls import path
from . import views

# http://127.0.0.1:8000/
urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('categories', views.categories, name='categories'),
    path('studentlogin', views.studentlogin, name='studentlogin'),
    path('instructorlogin', views.instructorlogin, name='instructorlogin'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
