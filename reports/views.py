from django.shortcuts import render
from profiles.models import Profile
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Report
from .utils import convert_image
from django.views.generic import ListView, DetailView


@login_required
def create_report_view(request):
    if request.is_ajax():
        name = request.POST.get('name')
        remarks = request.POST.get('remarks')
        b64_image = request.POST.get('image')  # get image from html in b64 format
        image = convert_image(b64_image)  # convert from b64 to db acceptable img
        author = Profile.objects.get(user=request.user)

        Report.objects.create(
            name=name,
            image=image,
            remarks=remarks,
            author=author
        )

        return JsonResponse({
            "msg": "got data"
        })

    return JsonResponse({
        "msg": "error in create_report_view"
    })


class ReportslistView(ListView):
    model = Report
    template_name = 'reports/home_list.html'
    context_object_name = 'reports_list'


class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/detail.html'
    context_object_name = 'report_obj'
