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
    url(r'^$', views.ZleceniaListView.as_view(), name='lista_zlecen'),
    url(r'^(?P<pk>[0-9]+)', views.ZleceniaDetailView.as_view(), name='szczegoly_zamowienia'),
    url(r'^(?P<pk>[0-9]+)/edytuj/$', views.ZlecenieUpdateView.as_view(), name='edytuj_zlecenie'),

    url(r'^(?P<pk>[0-9]+)/edytuj_adres/(?P<adres_id>[0-9]+)/$', views.AdresUpdateView.as_view(), name='edytuj_adres'),
]
