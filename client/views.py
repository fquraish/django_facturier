from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
# Create your views here.
from .models import Client
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import *
from django.forms import ModelForm



class ClientCreateView(CreateView):
    model = Client
    fields = ['first_name','last_name','tel','raison_social','siret','tva','email']
    redirect_field_name = 'next'
    success_url = reverse_lazy('client-list')

    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, ** kwargs)
        context["addresses_form"] = ClientAdressesForm()
        return context
    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            formToSave = ClientAdressesForm(self.request.POST,self.request.FILES, instance = self.object)
            if  formToSave.is_valid():
                form.save()
                formToSave.save()
               
                return HttpResponseRedirect(self.get_success_url())
        else :
            context = {
                'form' : form,
                'addresses_form': formToSave
            }
            return self.render_to_response(context)
  

    
class ClientListView(ListView):
    model = Client



class ClientUpdateView(UpdateView):
    model = Client
    fields = ['first_name','last_name','tel','raison_social','siret','tva','email']
    template_name = 'client/client_form.html'
    def get_success_url(self):
        return reverse_lazy("client-detail",args=[self.get_object().id])

    def get_context_data(self, **kwargs):
        context = UpdateView.get_context_data(self, ** kwargs)
        context["addresses_form"] = ClientAdressesForm(instance=self.get_object())
        return context
    
    def form_valid(self, form):
        formToSave = ClientAdressesForm(self.request.POST, instance = self.get_object())
        if form.is_valid() and formToSave.is_valid():
            self.new_user = form.save()
            formToSave.save()
            return HttpResponseRedirect(self.get_success_url())
        else :
            context = {
                'form' : form,
                'addresses_form': formToSave
            }
            return self.render_to_response(context)
    

class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client-list')
    



class ClientDetailView(DetailView):
    model = Client
    # def get_context_data(self, **kwargs):
    #     context = DetailView.get_context_data(self, ** kwargs)
    #     context["factures_list"] = Facture.objects.filter(Facture.client.id = self.get_object().client.id )
    #     return context


 

