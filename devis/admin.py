from django.contrib import admin
from devis.models import Devis, LigneDevis
from client.models import Client

# Register your models here.

class  LigneDevisInline(admin.TabularInline):
    model =  LigneDevis
    


class DevisAdmin(admin.ModelAdmin):
    
    inlines = [ LigneDevisInline]


admin.site.register(Devis,DevisAdmin )
