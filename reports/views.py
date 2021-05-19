from django.shortcuts import render
from profiles.models import Profile
from django.http import JsonResponse

from .models import Report
from .utils import convert_image


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


def all_reports_view(request):
    # todo see list of all reports
    pass
