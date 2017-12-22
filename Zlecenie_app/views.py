"""
Definition of views.
"""

from django.core.urlresolvers import reverse_lazy
from django.views import generic

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


