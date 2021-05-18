from django.shortcuts import render
from django.views.generic import ListView, DetailView

from reports.forms import ReportForm
from sales.models import Sale, Position
from .forms import SaleSearchForm
from django.db.models import Q

from .utils import sales_and_positions


def home_view(request):
    sale_form = SaleSearchForm(request.POST or None)
    report_form = ReportForm()
    data_main = by_id = customer = salesman = chart = None

    # allow to user search data for time periods
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')

        # all logic in util.py file
        data_main, by_id, customer, salesman, chart = sales_and_positions(date_from, date_to, chart_type, request)

    context = {
        'title': 'Sales Home',
        'sale_form': sale_form,
        'report_form': report_form,
        'data': data_main,
        "by_id": by_id,
        "by_customer": customer,
        "by_salesman": salesman,
        "chart": chart
    }

    return render(request, 'sales/home.html', context)


class SaleListView(ListView):
    model = Sale
    template_name = 'sales/main.html'
    context_object_name = 'sale_list'


class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'
    context_object_name = 'sale'
