from datetime import datetime

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import (
    login,
    logout)

import Account_app.views

admin.autodiscover()

urlpatterns = [
    url(r'^login/$', login, {

        'template_name': 'Account_app/login.html',
        'authentication_form': Account_app.forms.BootstrapAuthenticationForm,
        'extra_context':
            {
                'title': 'Logowanie',
                'year': datetime.now().year,
            }

    }, name='login'),
    url(r'^logout$', logout, {
        'next_page': '/',
    }, name='logout'),
    url(r'^singup/$', Account_app.views.singup, name='singup'),
    url(r'^profile/', Account_app.views.UserProfile_view.as_view(), name='profile'),
    url(r'^password_change/$', Account_app.views.change_password, name='change-password'),
    url(r'^edit/$', Account_app.views.edit_user, name='edytuj-profil'),
    url(r'^userCompany/(?P<pk>[0-9]+)$', Account_app.views.userCompanyUpdate.as_view(), name='company-update'),

    url(r'^userProfile/(?P<pk>[0-9]+)$', Account_app.views.userProfileUpdate.as_view(), name='userProfile-update'),



]
