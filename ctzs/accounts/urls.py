from django.urls import path
from . import views 
from accounts import views
from django.conf.urls import url

# Paths to views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path("profile/", views.profile, name="profile"), #profile view~subrat
    path("news/", views.news, name="news"), # news AJAX request
    path("grabnews/", views.grabnews, name="grabnews"), # news AJAX request
    url('sage/', views.sage, name="sage"),
    
]