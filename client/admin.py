from django.contrib import admin
from .models import Client,Addresses
from .forms import *



class AddressesInline(admin.TabularInline):
    model = Addresses 
    


class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name']
    inlines = [AddressesInline]




    
admin.site.register(Client,ClientAdmin)

