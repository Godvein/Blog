from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
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
        messages.success(request, "account was created successfully")
        return redirect("login")
        
    return render(request, "register.html")

def login(request):
    return render(request, "login.html")