"""
Definition of views.
"""
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views import generic

from .models import Adres


class AdresView(generic.ListView):
    template_name = 'Adres_app/adres_list.html'
    context_object_name = 'lista_adresow'

    def get_queryset(self):
        return Adres.objects.filter(user=self.request.user)


class AdresCreateView(generic.CreateView):
    model = Adres
    template_name = 'Adres_app/adres_form.html'
    success_url = reverse_lazy('Adres_app:lista_adresow')
    fields = ['nazwa', 'ulica', 'nr', 'kod_pocztowy', 'miasto']

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        self.object = form.save()
        return render(self.request, 'Adres_app/adres_list.html', {'adres': self.object})


class AdresUpdateView(generic.UpdateView):
    model = Adres
    template_name = 'Adres_app/adres_form.html'
    success_url = reverse_lazy('Adres_app:lista_adresow')
    fields = ['nazwa', 'ulica', 'nr', 'kod_pocztowy', 'miasto']


class AdresDeletaView(generic.DeleteView):
    model = Adres
    success_url = reverse_lazy('Adres_app:lista_adresow')
