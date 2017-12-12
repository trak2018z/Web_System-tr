"""
Definition of views.
"""

from django.views import generic

from .models import Lista_Zlecen, Zlecenie


class IndexView(generic.ListView):
    template_name = 'Klient_app/index.html'
    context_object_name = 'order_list'

    def get_queryset(self):
        return Zlecenie.objects.all()


class OrderDetailView(generic.DetailView):
    model = Lista_Zlecen
    template_name = 'Klient_app/detail.html'
