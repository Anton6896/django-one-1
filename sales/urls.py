from django.urls import path
from .views import (home_view, SaleListView, SalesDetailView,
                    upload_csv_files)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('sales/', SaleListView.as_view(), name='list'),
    path('sales/<int:pk>/', SalesDetailView.as_view(), name='detail'),
    path('upload_csv/', upload_csv_files, name='upload_csv'),

]
