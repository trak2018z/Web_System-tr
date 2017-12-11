from datetime import datetime
from django.contrib.auth.views import (
    login,
    logout,
    password_change,
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete)
import Account_magnament_app.views
from django.contrib import admin
from django.conf.urls import url, include

admin.autodiscover()

urlpatterns = [
    url(r'^login/$',
        login,
        {
            'template_name': 'Account_magnament_app/login.html',
            'authentication_form': Account_magnament_app.forms.BootstrapAuthenticationForm,
            'extra_context':
                {
                    'title': 'Logowanie',
                    'year': datetime.now().year,
                }
        },
        name='login'),
    url(r'^logout$',
        logout,
        {
            'next_page': '/',
        },
        name='logout'),

    url(r'^singup/$', Account_magnament_app.views.singup, name='singup'),
    url(r'^profile/$', Account_magnament_app.views.view_profile, name='profile'),
    url(r'^profile/edit/$', Account_magnament_app.views.edit_profile, name='edit_profile'),
    url(r'^profile/change-password/$', Account_magnament_app.views.change_password, name='change-password'),

    url(r'^password_reset/$',
        password_reset, {'template_name': 'Account_magnament_app/password-reset.html',
                        'post_reset_redirect': 'Account_magnament_app:password_reset_done',
                         'email_template_name': 'Account_magnament_app\password_reset_email.html'
                          },
        name='password_reset'),

    url(r'^password_reset/done/$',
        password_reset_done, {'template_name': 'Account_magnament_app/password-reset_done.html'},
        name='password_reset_done'),


    url(r'^password_reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$'
        , password_reset_confirm,
       { 'template_name': 'Account_magnament_app/password-reset_confirm.html',
         'post_reset_redirect': 'Account_magnament_app:password_reset_complete'
        },
        name='password_reset_confirm'),

    url(r'^password_reset/complete/$',
        password_reset_complete,
        {'template_name': 'Account_magnament_app/password-reset_complete.html'},
        name='password_reset_complete'),
    #url(r'^profile/edit1/(?P<slug>[\w-]+)/$', Account_magnament_app.views.view_UserProfile.as_view(), name='edit_profile1'),

]