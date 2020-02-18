from django.shortcuts import render
from django.views.generic.list import ListView
from facture.models import Facture

# Create your views here.

class FactureListView(ListView):
    model = Facture