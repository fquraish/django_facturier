from django.forms import inlineformset_factory
from devis.models import Devis, LigneDevis
from django import forms


DevisLigneForm = inlineformset_factory(Devis, LigneDevis,
                                            fields="__all__",
                                            can_delete = True,
                                            extra = 1



                                            )