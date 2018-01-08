from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # dane uzytkownika
    # image = models.ImageField(upload_to='profile_image', blank=True)
    nr_telefonu = models.IntegerField(default=0)
    ulica = models.CharField(max_length=200, default="")
    nr_domu = models.CharField(max_length=20, default=0)
    miasto = models.CharField(max_length=200, default="")
    kod_pocztowy = models.CharField(max_length=6, default="")
    # dane do faktury
    telefon_firmy = models.IntegerField(default=0)
    nazwa_firmy = models.CharField(max_length=300, blank=True)
    miasto_firmy = models.CharField(max_length=200, blank=True)
    ulica_firmy = models.CharField(max_length=200, blank=True)
    nr_firmy = models.CharField(max_length=20, blank=True)
    kod_pocztowy_firmy = models.CharField(max_length=6, blank=True)
    nip_firmy = models.IntegerField(default=0)

    def __str__(self):
        return self.user.get_username()


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
