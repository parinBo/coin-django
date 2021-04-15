from django.contrib import admin
from .models import *
# Register your models here.

class coinAdmin(admin.ModelAdmin):
    list_display = ['coin','price','pay']
    list_filter  = ['coin']


admin.site.register(AddCoin,coinAdmin)
admin.site.register(pocket)
admin.site.register(coin)

