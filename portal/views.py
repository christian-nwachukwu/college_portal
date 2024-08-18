from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
# Home page
def index(request):
    #   check to confirm login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #   authenticate
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


def logout_user(request):
    pass