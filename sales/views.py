from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sales.models import Sale
from .forms import SaleSearchForm


def home_view(request):
    form = SaleSearchForm(request.POST or None)
    return render(request, 'sales/home.html', {
        'title': 'Sales Home',
        'form': form
    })

class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sale_list'

class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    context_object_name = 'sale'
