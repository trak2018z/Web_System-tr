"""Web_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.AdresView.as_view(), name='lista_adresow'),
    # .adres/dodaj_adres
    url(r'^nowy_adres/$', views.AdresCreateView.as_view(), name='nowy_adres'),
    # .adres/edytuj_adres
    url(r'^(?P<pk>[0-9]+)/$', views.AdresUpdateView.as_view(), name='edytuj_adres'),
    # .adres/usun_adres
    url(r'^(?P<pk>[0-9]+)/usun$', views.AdresDeletaView.as_view(), name='usun_adres'),
]
