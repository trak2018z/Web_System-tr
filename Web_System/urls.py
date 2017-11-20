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
from datetime import datetime
import django.contrib.auth.views

import Info_app.views
import Login_app.forms
import Login_app.views
from django.contrib import admin
from django.conf.urls import url, include

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', Info_app.views.home, name='home'),
    url(r'^contact$', Info_app.views.contact, name='contact'),
    url(r'^about', Info_app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'Login_app/login.html',
            'authentication_form': Login_app.forms.BootstrapAuthenticationForm,
            'extra_context':
                {
                    'title': 'Logowanie',
                    'year': datetime.now().year,
                }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^singup/$', Login_app.views.singup, name='singup'),

]
