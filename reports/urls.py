from django.urls import path
from .views import (create_report_view, ReportslistView,
                    ReportDetailView, delete_report)

app_name = "reports"

urlpatterns = [
    path('create_report/', create_report_view, name="create_report"),
    path('list/', ReportslistView.as_view(), name="list"),
    path('detail/<int:pk>', ReportDetailView.as_view(), name="detail"),
    path('delete/', delete_report, name="delete_report"),

]
