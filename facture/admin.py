from django.contrib import admin
from facture.models import Facture, LigneFacture


# Register your models here.

class  LigneFactureInline(admin.TabularInline):
    model =  LigneFacture
    


class FactureAdmin(admin.ModelAdmin):
    
    inlines = [ LigneFactureInline]


admin.site.register(Facture,FactureAdmin )

# Register your models here.
