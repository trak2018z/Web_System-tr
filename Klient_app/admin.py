from django.contrib import admin

from Klient_app.models import Lista_Adresow, Lista_Zlecen, Zlecenie, Adres

admin.site.register([Lista_Zlecen,Adres,Zlecenie,Lista_Adresow])
