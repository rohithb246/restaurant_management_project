from django.contrib import admin
from .models import Restaurant

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "has_delivery")
    list_editable = ("has_delivery",)
    search_fields = ("name", "address")
    list_filter = ("is_active",)