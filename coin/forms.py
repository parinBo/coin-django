from django import forms
from django.core import validators


def check_size(value):
    if len(value) < 6:
        raise forms.ValidationError("the Password is too short")
def check_age(value):
    if value < 10 :
        raise forms.ValidationError("your age is so less")
def check_price(v):
    if v <= 0:
        raise forms.ValidationError("your price is wrong")
def check_pay(v):
    if v <= 0:
        raise forms.ValidationError("your pay is wrong")
coin_choice = [
    ('ada', 'ada'),
    ('btc', 'btc'),
    ('usdt', 'usdt'),
    ('iost', 'iost'),
    ('near', 'near'),
    ('wan', 'wan'),
]


class SignUp(forms.Form):
    first_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control','id':'test'}))
    email = forms.EmailField(help_text = 'write your email', required = False)
    Address = forms.CharField(required = False, )
    age = forms.IntegerField(required = False, validators = [check_age, ] )
    password = forms.CharField(widget = forms.PasswordInput, validators = [check_size, ])
    re_password = forms.CharField(widget = forms.PasswordInput, required = False)


class AddCoin(forms.Form):
    pay = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),validators = [check_pay, ] )
    price = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}),validators = [check_price ] )
    coin = forms.ChoiceField(choices=coin_choice,widget=forms.Select(attrs={'class': 'form-control'}))
    
    def clean_pay(self):
        pay = self.cleaned_data['pay']
        if pay<0:
             raise forms.ValidationError("your pay is wrong")
        return pay