from django.urls import path
from . import views 
from accounts import views
from django.conf.urls import url

# Paths to views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name="home"),
    path("profile/", views.profile, name="profile"), #profile view~subrat
    path("grabnews/", views.grabnews, name="grabnews"), # grab news for the dashboard
    url('sage/', views.sage, name="sage"),
    
]