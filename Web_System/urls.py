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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = [
                  url(r'^$', views.home_redirect, name='home_redirect'),
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^account/', include('Account_app.urls', namespace='Account_app')),
                  url(r'^home/', include('Info_app.urls', namespace='Info_app')),
                  url(r'^adres/', include('Adres_app.urls', namespace='Adres_app')),
                  url(r'^zlecenia/', include('Zlecenie_app.urls', namespace='Zlecenie_app')),
                  url('^', include('django.contrib.auth.urls')),

                  # url(r'^account/', include('django.contrib.auth.urls'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
