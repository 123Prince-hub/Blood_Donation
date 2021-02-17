from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LogInForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# This is Home views here.

# Home View
def home(request):
    return render(request, 'bldonation/home.html')

# About View
def about(request):
    return render(request, 'bldonation/about.html')

# Contact View
def contact(request):
    return render(request, 'bldonation/contact.html')

# Dashboard View
def dashboard(request):
    return render(request, 'bldonation/dashboard.html')

# LogOut View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Sign Up View
def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulations!! You have Successfully Registered.')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'bldonation/signup.html', {'form': form})

# Log In View
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LogInForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LogInForm()
        return render(request, 'bldonation/login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')