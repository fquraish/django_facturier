from django.db import models
from client.models import Client

# Create your models here.
class Devis(models.Model):
    client = models.ForeignKey(Client,null = True, blank = True, on_delete = models.CASCADE)

    def get_total_final_price(self):
        result = 0
        for ligne in self.lignedevis_set.all():
            result += ligne.get_total_item_price()
            

        return result



class LigneDevis(models.Model):
    devis = models.ForeignKey(Devis,null = True, blank = True, on_delete = models.CASCADE)
    description = models.CharField(max_length = 100)
    quantity = models.IntegerField(default = 1)
    price = models.IntegerField()
    

    def get_total_item_price(self):
        
        return int(self.quantity) * int(self.price)

