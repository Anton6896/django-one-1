from django.urls import path
from .views import (home_view, SaleListView, SalesDetailView, UploadTemplateView)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('sales/', SaleListView.as_view(), name='list'),
    path('upload/', UploadTemplateView.as_view(), name='upload'),
    path('sales/<int:pk>/', SalesDetailView.as_view(), name='detail'),


]
