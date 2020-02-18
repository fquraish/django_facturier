from django.db import models
from devis.models import Devis
from client.models import Client

# Create your models here.

class Facture(models.Model):
    devis = models.OneToOneField(Devis,null = True, blank = True ,on_delete = models.CASCADE)
    client = models.OneToOneField(Client,null = True, blank = True ,on_delete = models.CASCADE)


    


class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture,null = True, blank = True, on_delete = models.CASCADE)
    description = models.CharField(max_length = 100)
    quantity = models.IntegerField(default = 1)
    price = models.IntegerField()
    
  
    

   