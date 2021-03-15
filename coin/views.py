from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(req):
    return render(req,'index.html')


def register(req):
    if req.method == 'POST':
        data = req.POST
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        email = data.get('email')
        password = data.get('password')
        user = User()
        user.username = firstname
        user.email = email
        user.set_password(password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        return redirect('login')
    return render(req,'register.html')

@login_required
def addCoin(req):
    return render(req,'addCoin.html')