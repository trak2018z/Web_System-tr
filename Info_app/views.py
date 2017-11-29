"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpRequest
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Info_app/home.html',
        {
            'title': 'Strona Domowa',
            'year': datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Info_app/contact.html',
        {
            'title': 'Kontakt',
            'year': datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'Info_app/about.html',
        {
            'title': 'O nas',
            'message': 'Aplikacja wykonana została na potrzeby przedmiotu Aplikacje internetowe.',
            'year': datetime.now().year,
        }
    )
