from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from picstock.forms import LoginForm, CreateUserForm
from django.contrib import messages
# Create your views here.
def welcome(request):
    return render(request,'mini/welcome.html')

@login_required
def subscribehome(request):
    return render(request,'mini/subscribehome.html')

def send_email(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        recipient_list = []
        subject = "Jini Welcome"
        message = f"Thank you for registering {user_name.capitalize()}\n\nWelcome to the World of Jini"
        from_email = settings.EMAIL_HOST_USER
        users = user_email.split(',')
        for user in users:
            recipient_list.append(user)
        send_mail(subject,message,from_email,recipient_list,fail_silently=False)
        messages.success(request,"Subscribed!")
        return render(request,'mini/subscribed.html')
    else:
        return redirect(request, 'home.html')
    
###
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"User account created successfully!")
            return redirect("login")
    formvalue = {'registerform':form}
    return render(request,'mini/register.html',context=formvalue)

# -- Login Page
def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("welcome")
    formvalue = {'loginform':form}
    return render(request,'mini/login.html',context=formvalue)

# --Logout 
def logout(request):
    auth.logout(request)
    messages.success(request,"Logout Success!")
    return redirect("login")