"""
Definition of views.
"""

from django.views import generic

from .models import Zlecenie, Adres


class OrderView(generic.ListView):
    template_name = 'Klient_app/index.html'
    #template_name = 'Klient_app/index.html'
    context_object_name = 'lista_zlecen'

    def get_queryset(self):
        return Zlecenie.objects.filter(user=self.request.user)


class OrderDetailView(generic.DetailView):
    model = Zlecenie
    template_name = 'Klient_app/detail.html'

class AdresView(generic.ListView):
    template_name = 'Klient_app/ssss.html'
    context_object_name = 'lista_adresow'

    def get_queryset(self):
        return Adres.objects.filter(user=self.request.user)