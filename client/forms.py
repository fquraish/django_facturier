from django.forms import inlineformset_factory
from .models import Client,Addresses
from django import forms


ClientAdressesForm = inlineformset_factory(Client, Addresses,
                                            fields="__all__",
                                            can_delete = True,
                                            extra = 1



                                            )