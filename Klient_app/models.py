from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone


class Lista_Zlecen(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.get_username()

    def get_absolute_url(self):
        return reverse('order:order_detail',kwargs={'pk':self.pk})

class Lista_Adresow(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.get_username()

 #   def get_absolute_url(self):
#        return reverse('order:adres',kwargs={'pk':self.pk})

class Adres(models.Model):
    lista_adresow = models.ForeignKey(Lista_Adresow, blank=True)
    nazwa = models.CharField(max_length=200,blank=True)
    ulica = models.CharField(max_length=200)
    nr = models.CharField(max_length=20)
    miasto = models.CharField(max_length=200)
    kod_pocztowy = models.CharField(max_length=10)

    def __str__(self):
        return self.pk


class Zlecenie(models.Model):
    STATUS_CHOICES = (
        (1, 'Nowe'),
        (2, 'Przyjete'),
        (3, 'W oczekiwaniu na odbior'),
        (4, 'Dostawa'),
        (5, 'Zrealizowane'),
    )
    lista_zlecen = models.ForeignKey(Lista_Zlecen, on_delete=models.CASCADE)
    adres_odbioru = models.OneToOneField(Adres, related_name='odbior')
    adres_dostawy = models.OneToOneField(Adres, related_name='dostawa')
    status_zlecenia = models.IntegerField(choices=STATUS_CHOICES, default=1)
    data_zlozenia = models.DateTimeField(default=timezone.now())
    data_odbioru = models.DateTimeField()
    data_dostarczenia = models.DateTimeField()

    #def __str__(self):
     #   return self.lista_zlecen.user.
