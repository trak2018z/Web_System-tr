"""
Definition of views.
"""

import googlemaps
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import generic
from googlemaps import distance_matrix

from Adres_app.models import Adres
from Zlecenie_app.forms import ZleceniaForm, AdresForm
# from Zlecenie_app.forms import ZleceniaForm, AdresForm
from .models import Zlecenie


# dzialajace
@method_decorator(login_required, name='dispatch')
class ZleceniaListView(generic.ListView):
    template_name = 'Zlecenie_app/zlecenie_list.html'
    context_object_name = 'lista_zlecen'

    def get_queryset(self):
        if not self.request.user.groups.filter(name='Klient').exists():
            return Zlecenie.objects.all()
        else:
            return Zlecenie.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class ZleceniaDetailView(generic.DetailView):
    model = Zlecenie

    def get_queryset(self):
        if not self.request.user.groups.filter(name='Klient').exists():
            self.template_name = 'Zlecenie_app/kontroler.html'
            return Zlecenie.objects.all()

        else:
            self.template_name = 'Zlecenie_app/zlecenie_detail.html'
            return Zlecenie.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class ZlecenieCreate_newAdesView(generic.CreateView):
    model = Adres
    template_name = 'Zlecenie_app/zlecenie_form.html'
    success_url = reverse_lazy('Zlecenie_app:nowe_zlecenie')
    fields = ['nazwa', 'ulica', 'nr', 'kod_pocztowy', 'miasto']


@method_decorator(login_required, name='dispatch')
class ZlecenieUpdateView(generic.UpdateView):
    model = Zlecenie
    template_name = 'Zlecenie_app/zlecenie_form.html'
    fields = ['status_zlecenia', 'data_odbioru',
              'data_dostarczenia', 'wartosc']

    def get_success_url(self):
        return reverse_lazy('Zlecenie_app:szczegoly_zamowienia', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ZlecenieCreateView(generic.CreateView):
    template_name = 'Zlecenie_app/zlecenie_create.html'
    model = Zlecenie
    fields = ['ilosc_sztuk', 'waga', 'adres_odbioru', 'adres_dostawy', 'data_odbioru',
              'data_dostarczenia']

    success_url = reverse_lazy('Zlecenie_app:lista_zlecen')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        self.object = form.save()
        # send_mail('subject', 'body of the message', 'noreply@bottlenose.co', ['vitor@freitas.com'])
        return HttpResponseRedirect(self.get_success_url())


# do poprawki
@method_decorator(login_required, name='dispatch')
class ZlecenieUpdateView2(generic.UpdateView):
    template_name = 'Zlecenie_app/zlecenie_form.html'

    def get_initial(self):
        gmap = googlemaps.Client(key='AIzaSyAewSjMOfSLupwSWSJvkpvR4-WD5t59K1Y')
        dit = distance_matrix.distance_matrix(gmap, 'Stalowa Wola', 'Sandomierz')
        dist = dit['rows'][0]['elements'][0]['duration']['text']
        return {
            'data_dostarczenia': dist
        }

    def get(self, request, *args, **kwargs):
        return self.render_to_response(
            {'adresform': AdresForm(prefix='adresform_pre'), 'zlecenieform': ZleceniaForm(prefix='zlecenieform_pre')})

    def post(self, request, *args, **kwargs):
        adresform = _get_form(request, AdresForm, 'aform_pre')
        zlecenieform = _get_form(request, ZleceniaForm, 'bform_pre')
        if adresform.is_bound and adresform.is_valid():
            adresform.save()
        # Process adresform and render response
        elif zlecenieform.is_bound and zlecenieform.is_valid():
            zlecenieform.save()
        # Process zlecenieform and render response
        return self.render_to_response({'adresform': adresform, 'zlecenieform': zlecenieform})


def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)
