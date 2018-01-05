from datetime import datetime


from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete)

import Account_app.views

admin.autodiscover()

urlpatterns = [
    url(r'^login/$',login,{

            'template_name': 'Account_app/login.html',
            'authentication_form': Account_app.forms.BootstrapAuthenticationForm,
            'extra_context':
                {
                    'title': 'Logowanie',
                    'year': datetime.now().year,
                }

        },name='login'),
    url(r'^logout$',logout,{
            'next_page': '/',
        },name='logout'),
    url(r'^singup/$', Account_app.views.singup, name='singup'),
    url(r'^profile/$', Account_app.views.view_profile, name='profile'),
    url(r'^profile/edit/$', Account_app.views.edit_profile, name='edit_profile'),
    url(r'^password_change/$', Account_app.views.change_password, name='change-password'),

]