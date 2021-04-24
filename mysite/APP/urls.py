from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('library', views.library, name='library'),
    path('geography', views.geography, name='geography'),
    path('age', views.age, name='age'),
    path('phone', views.phone, name='phone'),
    path('environment', views.environment, name='environment'),
    path('recognition', views.recognition, name='recognition'),
    path('upload/', views.upload, name='upload'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('file_list/', views.file_list, name='file_list'),
    path('spectrum_map/', views.spectrum_map, name='spectrum_map'),
    path('model/', views.model, name='model'),
]