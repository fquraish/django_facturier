from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    raison_social = models.CharField(max_length=30)
    siret = models.IntegerField()
    tva = models.CharField(max_length=30)
    email = models.CharField(max_length=30)

class Addresses(models.Model):
    client = models.ForeignKey(Client,null = True, blank = True, related_name = 'addresses', on_delete = models.CASCADE)
    zipcode = models.CharField(max_length=30,null = True, blank = True )
    city = models.CharField(max_length=30 ,null = True, blank = True)
    street = models.CharField(max_length=30, null = True, blank = True)

