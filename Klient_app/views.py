"""
Definition of views.
"""

from django.views import generic

from .models import Zlecenie


class IndexView(generic.ListView):
    template_name = 'Klient_app/index.html'
    context_object_name = 'order_list'

    def get_queryset(self):
        return Zlecenie.objects.filter(user=self.request.user)


class OrderDetailView(generic.DetailView):
    model = Zlecenie
    template_name = 'Klient_app/detail.html'
