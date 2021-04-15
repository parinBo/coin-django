from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from ..forms import AddCoin


def mycoin(request):
    return render(request,"coin/mycoin.html")

def history(request):
    return render(request,"coin/history.html")


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
    return render(request, 'coin/addCoin.html', {'form': form})