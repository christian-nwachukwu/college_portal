from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
# Home page
def index(request):
    #   check to confirm login username and password
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #   authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful!')
            return redirect('index')
        else:
            messages.success(request, 'Login Error, please try again')
            return redirect('index')
        
    else:
        return render(request, 'index.html', {})    # Render the html files. Add the template folder to setting.py. Create html files in templates folder



#   Create Logout logic
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out...")
    return redirect('index')


#   create register logic
def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #   lets authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration Successful!')
            return redirect('index')
        
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})