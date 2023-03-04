from django.contrib.auth import login,logout
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import  messages
from .forms import UserLoginForm,UserRegisterForm

def index(request):
    return render(request, 'register/index.html')




def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,"login user")
            return redirect('/')
        else:
            messages.error(request,'Error Login')
    else:
        form = UserLoginForm()
        return render(request,'register/login.html',{'form':form})





def user_logout(request):
        logout(request)
        return redirect('login')





def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register Success')
            return redirect('login')
        else:
            messages.error(request, 'Register Error')
    else:
        form = UserRegisterForm()
    return render(request, 'register/register.html', {'form':form})




