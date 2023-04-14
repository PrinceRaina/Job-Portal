from django.shortcuts import render
from .models import *
import re
from django.http import HttpResponse
import random
# Create your views here.

def Signup(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        mobile=request.POST["mobile"]
        if len(password)<8:
            return False 
        if not re.search(r'[A-Z]', password):
            return False
    
        # Contains at least one lowercase letter
        if not re.search(r'[a-z]', password):
            return False
        
        # Contains at least one digit
        if not re.search(r'\d', password):
            return False
        
        # Contains at least one special character
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False
        
        # All criteria met
        user=signup(email=email,password=password,name=name,mobile=mobile)
        user.save()
        return HttpResponse("chal gaya")

    return render(request,"signup.html")

def Login(request):

    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        user=signup.objects.get(email=email,password=password)
        if user is not None:
            return HttpResponse("login ho gya")

    return render(request,"login.html")

def Home(request):
    return render(request,"home.html")

def Otp():
    otp=""
    for i in range(4):
        otp = otp + random.randint(0,9)
    return otp      

def Mob(request):
    if request.method == "POST":
        if "mobile" in request.POST:
            mobile=request.POST["mobile"]
            mob=signup.objects.get(mobile=mobile) 
            if mob:
                otp_value=Otp()
                otp=signup.objects.create(otp=otp_value)
                otp.save()
            
    return render(request,"Mobile.html")

def verify(request):
    return render(request,"Otp.html")
