from django.contrib import admin
from .models import ResaleFlat


# Register your models here.
@admin.register(ResaleFlat)
class ResaleFlatAdmin(admin.ModelAdmin):
    list_display = ("town", "flat_type", "resale_price", "lease_commence_date")
    search_fields = ("town", "flat_type", "block", "street_name")
