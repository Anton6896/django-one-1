from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from reports.forms import ReportForm
from sales.models import Sale
from .forms import SaleSearchForm

from .utils.utils import sales_and_positions


def home_view(request):
    sale_form = SaleSearchForm(request.POST or None)
    report_form = ReportForm()
    data_all = by_id = by_date = chart = None

    # allow to user search data for time periods
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        result_by = request.POST.get('result_by')

        # all logic in util.py file
        if sales_and_positions(date_from, date_to, chart_type, result_by, request):
            data_all, by_id, by_date, chart = sales_and_positions(date_from, date_to, chart_type, result_by, request)

    context = {
        'title': 'Sales Home',
        'sale_form': sale_form,
        'report_form': report_form,
        'data': data_all,
        "by_id": by_id,
        "by_date": by_date,
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


class UploadTemplateView(TemplateView):
    """
    using js for the dropzone from https://www.dropzonejs.com/#usage
    i took all dropzone.css and dropzone.js from package
    using in static/dropzone/...
    """
    template_name = 'sales/from_file.html'


def upload_csv_files(request):
    return HttpResponse()
