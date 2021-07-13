from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here

def index(request):
    return render(request, 'home.html')

def user_register(request):

    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        user = User.objects.create_user(first_name = fname, last_name = lname, username = uname, email = email ,password=pass1)
        user.save()
        return redirect('/login')
    
    return render(request, 'register.html')
    

def user_login(request):
    return render(request, 'login.html')