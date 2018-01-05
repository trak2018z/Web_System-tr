from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # dane uzytkownika
    image = models.ImageField(upload_to='profile_image', blank=True)
    phone = models.IntegerField(default=0)
    street = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    post_code = models.CharField(max_length=6, default="")
    # dane do faktury
    company = models.CharField(max_length=300, blank=True)
    company_city = models.CharField(max_length=200, blank=True)
    company_street = models.CharField(max_length=200, blank=True)
    company_post_code = models.CharField(max_length=6, blank=True)
    company_nip = models.IntegerField(default=0)

    def __str__(self):
        return self.user.get_username()


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
