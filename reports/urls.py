from django.urls import path
from .views import create_report_view

app_name = "reports"

urlpatterns = [
    path('create_report/', create_report_view, name="create_report"),

]
