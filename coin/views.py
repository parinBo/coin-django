from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SignUp,AddCoin
from .models import  AddCoin as coin
def home(req):
    a = coin.objects.all()
    return render(req,'index.html',{'data':a})



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

@login_required
def addcoin(request):
    form = AddCoin()
    if request.method == 'POST':
        form = AddCoin(request.POST)
        if form.is_valid():
            hi='test'
            print(request.POST)
            print("wow")
        else:
            form = AddCoin(request.POST)
    return render(request, 'addCoin.html', {'form': form})