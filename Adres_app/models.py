from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Adres(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    nazwa = models.CharField(max_length=200, blank=True)
    ulica = models.CharField(max_length=200)
    nr = models.CharField(max_length=20)
    miasto = models.CharField(max_length=200)
    kod_pocztowy = models.CharField(max_length=10)

    def __str__(self):
        return self.nazwa

    def get_absolute_url(self):
        return reverse('Adres_app:lista_adresow', kwargs={'pk': self.pk})

    class Meta:
        unique_together = ('user', 'nazwa',)
