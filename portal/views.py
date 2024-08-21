from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.core.mail import send_mail

# Create your views here.
# Home page
def index(request):
    #   Grab everything in the database table
    records = Record.objects.all()



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
        return render(request, 'index.html', {'records':records})    # Render the html files. Add the template folder to setting.py. Create html files in templates folder



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


#   Return a customer record
def customer_record(request, pk):
    if request.user.is_authenticated:
        #   look up record
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'You have to be logged in to view record')
        return redirect('index')
    


#   Delete a customer record
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_item = Record.objects.get(id=pk)
        delete_item.delete()
        messages.success(request, 'Record deleted successfully...')
        return redirect('index')
    else:
        messages.success(request, 'You must be logged in to delete record...')
        return redirect('index')
    

#   Add new customer record
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                #   Send email if any (Optional - No code here...)
                messages.success(request, 'Record added successfully...')
                return redirect('index')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, 'You must be logged In...')
        return redirect('index')
    

#   Modify/Update record
def modify_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Record Has Been Updated!")
			return redirect('index')
		return render(request, 'modify_record.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('index')
