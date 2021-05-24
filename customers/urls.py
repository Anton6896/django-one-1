from django.urls import path
from .views import home

app_name = 'customers'

urlpatterns = [
    path('home/', home, name='home'),

]
