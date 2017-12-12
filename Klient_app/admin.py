from django.contrib import admin

from Klient_app.models import Zlecenie, Adres

admin.site.register([Adres,Zlecenie])
