from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from ..Models.bitkub import Bitkub 
from pprint import pprint

def home(req):
    coins = Bitkub.coins()
    pprint(coins)
    return render(req,'index.html',{"coins":coins})

def register(request):
    if request.method == 'POST':
        data = request.POST
        terms =  data.get('terms')
        if(terms=='on'):
            print("can regis")
            user = User()
            user.username = data.get('username')
            user.first_name = data.get('firstname')
            user.last_name = data.get('lastname')
            user.email = data.get('email')
            user.set_password(data.get('password'))
            try:
                user.save()
            except :
                print(NameError)
            messages.success(request, 'Good')
        else:
            messages.error(request, 'Error! you cannot regis ')
            return redirect('home')
    return render(request,'login.html')


