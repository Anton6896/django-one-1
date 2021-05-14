from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sales.models import Sale
from .forms import SaleSearchForm
from django.db.models import Q
import pandas as pd


def home_view(request):
    form = SaleSearchForm(request.POST or None)

    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')

        qs = Sale.objects.filter(Q(created__date__gte=date_from), Q(created__date__lte=date_to))
        df = pd.DataFrame(qs.values())

    return render(request, 'sales/home.html', {
        'title': 'Sales Home',
        'form': form,

    })


class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sale_list'


class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    context_object_name = 'sale'
