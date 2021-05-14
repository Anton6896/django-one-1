from django.contrib import admin
from .models import Position, Csv, Sale

# Register your models here.
admin.site.register(Position)
admin.site.register(Csv)
admin.site.register(Sale)
