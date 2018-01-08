"""
Definition of views.
"""
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import generic

from .models import Adres


@method_decorator(login_required, name='dispatch')
class AdresView(generic.ListView):
    template_name = 'Adres_app/adres_list.html'
    context_object_name = 'lista_adresow'

    def get_queryset(self):
        lista_adresow = Adres.objects.filter(user=self.request.user)
        query = self.request.GET.get("q")
        qmiasto = self.request.GET.get("qmiasto")
        if query:
            return lista_adresow.filter(
                Q(nazwa__icontains=query)
            ).distinct()
        if qmiasto:
            return lista_adresow.filter(
                Q(miasto__icontains=qmiasto)
            ).distinct()
        else:
            return lista_adresow


@method_decorator(login_required, name='dispatch')
class AdresCreateView(generic.CreateView):
    model = Adres
    template_name = 'Adres_app/adres_form.html'
    success_url = reverse_lazy('Adres_app:lista_adresow')
    fields = ['nazwa', 'ulica', 'nr', 'kod_pocztowy', 'miasto']

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name='dispatch')
class AdresUpdateView(generic.UpdateView):
    model = Adres
    template_name = 'Adres_app/adres_form.html'
    success_url = reverse_lazy('Adres_app:lista_adresow')
    fields = ['nazwa', 'ulica', 'nr', 'kod_pocztowy', 'miasto']


@method_decorator(login_required, name='dispatch')
class AdresDeletaView(generic.DeleteView):
    model = Adres
    success_url = reverse_lazy('Adres_app:lista_adresow')
