"""
Definition of views.
"""

from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import generic

from Adres_app.models import Adres
from Zlecenie_app.forms import ZleceniaForm
# from Zlecenie_app.forms import ZleceniaForm, AdresForm
from .models import Zlecenie


# dzialajace
@method_decorator(login_required, name='dispatch')
class ZleceniaListView(generic.ListView):
    context_object_name = 'lista_zlecen'

    def get_queryset(self):
        if not self.request.user.groups.filter(name='Klient').exists():
            self.template_name = 'Zlecenie_app/zlecenie_kontroler_list.html'
            return Zlecenie.objects.all()
        else:
            self.template_name = 'Zlecenie_app/zlecenie_list.html'
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
    # model = Zlecenie

    form_class = ZleceniaForm
    success_url = reverse_lazy('Zlecenie_app:lista_zlecen')

    def get_form_kwargs(self):
        kwargs = super(ZlecenieCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        #form.fields['adres_odbioru'] = Adres.objects.filter(user=user)
        self.object = form.save()
        # send_mail('subject', 'body of the message', 'noreply@bottlenose.co', ['vitor@freitas.com'])
        return HttpResponseRedirect(self.get_success_url())


# dodawanie dla operatora nie dziala na potem
@method_decorator(login_required, name='dispatch')
class ZlecenieKontrolerCreateView(generic.CreateView):
    template_name = 'Zlecenie_app/zlecenie_create_kontroler.html'
    model = Zlecenie
    fields = ['user', 'ilosc_sztuk', 'waga', 'adres_odbioru', 'adres_dostawy', 'data_odbioru',
              'data_dostarczenia']

    success_url = reverse_lazy('Zlecenie_app:lista_zlecen')

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        self.object = form.save()
        # send_mail('subject', 'body of the message', 'noreply@bottlenose.co', ['vitor@freitas.com'])
        return HttpResponseRedirect(self.get_success_url())
