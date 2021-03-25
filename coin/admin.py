from django.contrib import admin
from .models import AddCoin
# Register your models here.

class coinAdmin(admin.ModelAdmin):
    list_display = ['coin','price','pay']
    list_filter  = ['coin']
admin.site.register(AddCoin,coinAdmin)