from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sales.models import Sale, Position
from .forms import SaleSearchForm
from django.db.models import Q

from .utils import sales_and_positions


def home_view(request):
    form = SaleSearchForm(request.POST or None)
    data_html = None

    # allow to user search data for time periods
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')

        # all logic in util.py file
        data_html = sales_and_positions(date_from, date_to, chart_type, request)

    return render(request, 'sales/home.html', {
        'title': 'Sales Home',
        'form': form,
        'data': data_html,
    })


class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sale_list'


class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    context_object_name = 'sale'
