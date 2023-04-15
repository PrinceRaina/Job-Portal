from django.contrib import admin
from django.urls import path
from .views import *    

urlpatterns = [
    path("signup", Signup, name="signup"),
    path("login",Login, name="login"),
    # path("home",Home,name="home"),
    # path("mobile", Mobile,name="mobile"),
    # path("verify",verify,name="verify")
]
