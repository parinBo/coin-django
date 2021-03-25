from django.db import models  

coin_choice = [
    ('ada', 'ada'),
    ('btc', 'btc'),
    ('usdt', 'usdt'),
    ('iost', 'iost'),
    ('near', 'near'),
    ('wan', 'wan'),
]
class AddCoin(models.Model):
    pay = models.IntegerField(default=1)
    price = models.IntegerField(default=1)
    coin = models.CharField(max_length=50,choices=coin_choice,default='ada')
  