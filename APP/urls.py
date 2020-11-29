from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recognition', views.recognition, name='recognition'),
    path('upload/', views.upload, name='upload'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('file_list/', views.file_list, name='file_list'),
]