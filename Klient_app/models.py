from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# class Lista_Zlecen(models.Model):
#     user = models.OneToOneField(User)
#
#     def __str__(self):
#         return self.user.get_username()
#
#     def get_absolute_url(self):
#         return reverse('order:order_detail',kwargs={'pk':self.pk})
#
# class Lista_Adresow(models.Model):
#     user = models.OneToOneField(User)
#
#     def __str__(self):
#         return self.user.get_username()
#
#  #   def get_absolute_url(self):
# #        return reverse('order:adres',kwargs={'pk':self.pk})

class Adres(models.Model):
    user = models.ForeignKey(User, blank=True,null=True)
    nazwa = models.CharField(max_length=200,blank=True)
    ulica = models.CharField(max_length=200)
    nr = models.CharField(max_length=20)
    miasto = models.CharField(max_length=200)
    kod_pocztowy = models.CharField(max_length=10)

    def __str__(self):
        return self.nazwa


class Zlecenie(models.Model):
    NOWE=1
    PRZYJETE=2
    DO_ODBIORU=3
    DOSTAWA=4
    ZREALIZOWANE=5

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
    wartosc=models.FloatField(default=0.0)
    faktura=models.IntegerField(default=0)

    #def __str__(self):
     #   return self.lista_zlecen.user.