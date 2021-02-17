from django.contrib import admin
from .models import Donor

# Register your models here.
@admin.register(Donor)
class DonorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'desc']