from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from sales.models import Sale


def home_view(request):
    return render(request, 'sales/home.html', {'title': 'Sales Home'})


class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sale_list'


class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    context_object_name = 'sale'


