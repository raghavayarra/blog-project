from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name =  request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken!!!!')
                return redirect ('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already Taken!!')
                return redirect ('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                user.save()
                messages.info(request,'user created!!')
                return redirect('login')
        else:
            messages.info(request,'password wrong!!')
            return redirect('register')
    else:
        return render(request,'accounts/register.html')


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request,'invalid creditentials!!!!')
            return redirect('login')

    else:
        return render(request,'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')