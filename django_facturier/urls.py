"""django_facturier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from client.views import ClientCreateView,ClientListView,ClientDetailView,ClientUpdateView,ClientDeleteView
from devis.views import DevisListView,DevisDetailView,DevisCreateView,DevisUpdateView,DevisDeleteView, DevisPDFView
from facture.views import FactureListView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', ClientListView.as_view(), name='client-list'),
    path('new/', ClientCreateView.as_view(), name='client-create'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('client/<int:pk>/edit', ClientUpdateView.as_view(), name='client-update'),
    path('client/<int:pk>/delete', ClientDeleteView.as_view(), name='client-delete'),
    path('devis/', DevisListView.as_view(), name='devis-list'),
    path('devis/<int:pk>/', DevisDetailView.as_view(), name='devis-detail'),
    path('newdevis/', DevisCreateView.as_view(), name='devis-create'),
    path('devis/<int:pk>/edit', DevisUpdateView.as_view(), name='devis-update'),
    path('devis/<int:pk>/delete', DevisDeleteView.as_view(), name='devis-delete'),
    path('devis/<int:pk>/pdf', DevisPDFView.as_view(), name='devis-pdf'),
    path('factures/', FactureListView.as_view(), name='facture-list'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)