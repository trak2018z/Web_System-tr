from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from Adres_app.models import Adres


class Zlecenie(models.Model):
    NOWE = 1
    PRZYJETE = 2
    DO_ODBIORU = 3
    DOSTAWA = 4
    ZREALIZOWANE = 5

    STATUS_CHOICES = (
        (NOWE, 'Nowe'),
        (PRZYJETE, 'Przyjete'),
        (DO_ODBIORU, 'W oczekiwaniu na odbior'),
        (DOSTAWA, 'Dostawa'),
        (ZREALIZOWANE, 'Zrealizowane'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    adres_odbioru = models.ForeignKey(Adres, related_name='odbior')
    adres_dostawy = models.ForeignKey(Adres, related_name='dostawa')
    status_zlecenia = models.IntegerField(choices=STATUS_CHOICES, default=1)
    data_zlozenia = models.DateTimeField(default=timezone.now())
    data_odbioru = models.DateTimeField()
    data_dostarczenia = models.DateTimeField()
    wartosc = models.FloatField(default=0.0)
    ilosc_sztuk = models.IntegerField(default=0)
    waga = models.FloatField(default=0)
    dystans = models.FloatField(default=0)
    faktura = models.IntegerField(default=0)


    # def __str__(self):
    #   return self.lista_zlecen.user.
