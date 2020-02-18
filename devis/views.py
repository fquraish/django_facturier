from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from devis.models import Devis
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .forms import *
from django.http import HttpResponseRedirect
from django_weasyprint import WeasyTemplateResponseMixin
from django_weasyprint.views import CONTENT_TYPE_PNG



# Create your views here.

class DevisListView(ListView):
    model = Devis

class DevisDetailView(DetailView):
    model = Devis

class DevisPDFView(WeasyTemplateResponseMixin, DevisDetailView):
    # output of MyModelView rendered as PDF with hardcoded CSS
    # pdf_stylesheets = [
    #     settings.STATIC_ROOT + 'css/app.css',
    # ]
    # show pdf in-line (default: True, show download dialog)
    pdf_attachment = False
    # suggested filename (is required for attachment!)
    pdf_filename = 'foo.pdf'
    def get_context_data(self, **kwargs):
        context = DetailView.get_context_data(self, ** kwargs)

        context['pdf']= True
        return context
        

class DevisCreateView(CreateView):
    model = Devis
    fields = ['client']
    redirect_field_name = 'next'
    success_url = reverse_lazy('devis-list')
    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, ** kwargs)
        context["devisligne_form"] = DevisLigneForm()
        return context
    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            formToSave = DevisLigneForm(self.request.POST,self.request.FILES, instance = self.object)
            if  formToSave.is_valid():
                form.save()
                formToSave.save()
               
                return HttpResponseRedirect(self.get_success_url())
        else :
            context = {
                'form' : form,
                'devisligne_form': formToSave
            }
            return self.render_to_response(context)
class DevisUpdateView(UpdateView):
    model = Devis
    fields = ['client']
    template_name = 'devis/devis_form.html'
    def get_success_url(self):
        return reverse_lazy("devis-detail",args=[self.get_object().id])

    def get_context_data(self, **kwargs):
        context = UpdateView.get_context_data(self, ** kwargs)
        context["devisligne_form"] = DevisLigneForm(instance=self.get_object())
        return context
    
    def form_valid(self, form):
        formToSave = DevisLigneForm(self.request.POST, instance = self.get_object())
        if form.is_valid() and formToSave.is_valid():
            self.new_user = form.save()
            formToSave.save()
            return HttpResponseRedirect(self.get_success_url())
        else :
            context = {
                'form' : form,
                'devisligne_form': formToSave
            }
            return self.render_to_response(context)

class DevisDeleteView(DeleteView):
    model = Devis
    success_url = reverse_lazy('devis-list')

