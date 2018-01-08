from django.forms import ModelForm

from Adres_app.models import Adres
from Zlecenie_app.models import Zlecenie


class ZleceniaForm(ModelForm):
    class Meta:
        model = Zlecenie
        fields = ['ilosc_sztuk', 'waga', 'adres_odbioru', 'adres_dostawy', 'data_odbioru',
                  'data_dostarczenia']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ZleceniaForm, self).__init__(*args, **kwargs)
        self.fields['adres_dostawy'].queryset = Adres.objects.filter(user=user)
        self.fields['adres_odbioru'].queryset = Adres.objects.filter(user=user)


class AdresForm(ModelForm):
    class Meta:
        model = Adres
        fields = ['ulica', 'nr', 'kod_pocztowy', 'miasto']
