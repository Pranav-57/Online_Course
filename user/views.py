from django.shortcuts import render, redirect
from .forms import Registration, loginform, ProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

# Create your views here.
def registration(request):
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration Successful.')
            return redirect('login')
    else:
        form = Registration()
    return render(request, 'user/registration.html',{'form':form})

def userlogin(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = loginform(request.POST)
        if request.POST['email'] and request.POST['password']:
            if form.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(email=email, password=password)
                print('user')
                if user:
                    login(request, user)
                    messages.success(request,'Login Successfully.')
                    return redirect('home')
            else:
                messages.error(request,'Invalid username and password.')
                return redirect('login')  
        else:
            messages.error(request,'Fill both field')
            return redirect('login')  
    else:
        form = loginform()
    return render(request, 'user/login.html',{'form':form})

def userlogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logout Successfully.')
        return redirect('home')
    return redirect('login')

def userprofile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProfileForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid:
                form.save()
                return redirect('home')
        
        else:
            form = ProfileForm(instance=request.user)
            return render(request,'user/profile.html',{'form':form})
    else:
        return redirect('login')

def changepassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request,'user/changepassword.html',{'form':form})
    
    else:
        return redirect('login')