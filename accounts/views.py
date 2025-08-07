from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid credintials")
            return redirect("login")
    else:
        return render(request,"login.html")
    
def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        username=request.POST.get("username")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        context={first_name:first_name,
                 last_name:last_name,
                 email:email,
                 username:username
                 }
        if password1==password2:
            if User.objects.filter(username=username).exists():
                context["username_error"]="Username already exists"
                return render(request,"register.html",context)
            elif User.objects.filter(email=email).exists():
                context["email_error"]="email already exists"
                return render(request,"register.html",context)
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
                user.save()
                return redirect("/")
        else:
            context["password_error"]="password doesn't match"
            return render(request,"register.html",context)
    else:
        return render(request,"register.html")
    
def logout(request):
    auth.logout(request)
    return redirect("/")