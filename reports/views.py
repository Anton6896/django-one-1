from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
from profiles.models import Profile
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Report
from .utils import convert_image
from django.views.generic import ListView, DetailView
from .utils import link_callback
from django.contrib import messages


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
    ordering = ['-created']
    template_name = 'reports/list.html'
    context_object_name = 'reports_list'


class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/detail.html'
    context_object_name = 'report_obj'


def delete_report(request):
    if request.is_ajax():
        pk = request.POST.get('pk')
        report = Report.objects.get(pk=pk)

        # this user can delete ?
        if request.user == report.author.user:
            report.delete()
            messages.success(request, f'report was completely deleted !')
            # django das not redirecting user for this point , with this approach
            # i can do that with delete_view but not with ajax
            # for now its use the hardcoded redirection to heroku by js
            return JsonResponse({
                'status': 1, 'message': "great"
            })

    messages.warning(request, f'have some issue with this  !')
    return JsonResponse({
        'status': 0, 'message': "Server error"
    })


def render_pdf_view(request):
    template_path = 'reports/pdf_to.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
