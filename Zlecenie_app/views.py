"""
Definition of views.
"""
import googlemaps
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views import generic
from googlemaps import distance_matrix

from Adres_app.models import Adres
from Zlecenie_app.forms import ZleceniaForm, AdresForm
# from Zlecenie_app.forms import ZleceniaForm, AdresForm
from .models import Zlecenie


class ZleceniaListView(generic.ListView):
    template_name = 'Zlecenie_app/zlecenie_list.html'
    context_object_name = 'lista_zlecen'

    def get_queryset(self):
        if not self.request.user.groups.filter(name='Klient').exists():
            return Zlecenie.objects.all()
        else:
            return Zlecenie.objects.filter(user=self.request.user)


class ZleceniaDetailView(generic.DetailView):
    model = Zlecenie

    # template_name = 'Zlecenie_app/tmp.html'


    def get_queryset(self):
        if not self.request.user.groups.filter(name='Klient').exists():
            self.template_name = 'Zlecenie_app/kontroler.html'
            return Zlecenie.objects.all()

        else:
            self.template_name = 'Zlecenie_app/zlecenie_detail.html'
            return Zlecenie.objects.filter(user=self.request.user)


            # dla operatora
            # class AdresCreateView(generic.CreateView):
            #     model = Adres
            #     template_name = 'Adres_app/adres_form.html'
            #     success_url = reverse_lazy('Adres_app:lista_adresow')
            #     fields = ['nazwa', 'ulica', 'nr', 'kod_pocztowy', 'miasto']
            #
            #     def form_valid(self, form):
            #         user = self.request.user
            #         form.instance.user = user
            #         self.object = form.save()
            #         return render(self.request, 'Adres_app/adres_list.html', {'adres': self.object})

            # class ZleceniaDetailView(generic.DetailView):
            #   model = Zlecenie
            # template_name = 'Zlecenie_app/tmp.html'


class ZlecenieUpdateView(generic.UpdateView):
    model = Zlecenie
    template_name = 'Zlecenie_app/zlecenie_form.html'
    fields = ['status_zlecenia', 'data_odbioru',
              'data_dostarczenia', 'wartosc']

    def get_success_url(self):
        return reverse_lazy('Zlecenie_app:szczegoly_zamowienia', kwargs={'pk': self.object.pk})


class AdresUpdateView(generic.UpdateView):
    model = Adres
    template_name = 'Zlecenie_app/adres_form.html'
    form_class = AdresForm

    def get_success_url(self):
        return reverse_lazy('Zlecenie_app:szczegoly_zamowienia', kwargs={'pk': self.object.pk})


def _get_form(request, formcls, prefix):
    data = request.POST if prefix in request.POST else None
    return formcls(data, prefix=prefix)


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


class ZlecenieCreateView(generic.CreateView):
    model = Zlecenie
    template_name = 'Zlecenie_app/zlecenie_create.html'
    success_url = reverse_lazy('Zlecenie_app:lista_zlecen')
    fields = ['adres_odbioru', 'adres_dostawy']

    def get_initial(self):
        gmap = googlemaps.Client(key='AIzaSyAewSjMOfSLupwSWSJvkpvR4-WD5t59K1Y')
        dit = distance_matrix.distance_matrix(gmap, 'Stalowa Wola', 'Sandomierz')
        dist = dit['rows'][0]['elements'][0]['duration']['text']
        return {
            'data_dostarczenia': dist
        }

    def form_valid(self, form):
        user = self.request.user

        form.instance.user = user
        self.object = form.save()
        return render(self.request, {'zlecenie': self.object})

    template_name = 'Zlecenie_app/zlecenie_form.html'

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
