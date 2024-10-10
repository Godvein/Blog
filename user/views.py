from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
# Create your views here.
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, "register.html")

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, "register.html")
        

        user = User.objects.create_user(username= username, email= email, password= password)
        user.save()
        messages.success(request, "account was created successfully please login")
        return redirect("login")
        
    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "succefully logged in as " + username )
            return redirect("home")
        else:
            messages.error(request, "error logging in")
    return render(request, "login.html")

def logout(request):
    auth_logout(request)
    return redirect("login")

def profile(request):
    return render(request, "profile.html")

def editprofile(request):
    return render(request, "editprofile.html")