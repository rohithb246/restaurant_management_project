from django.contrib import admin
from .models import Order

@admin.action(description="Mark selected orders as processed")
def mark_orders_processed(modeladmin, request, queryset):
    updated_count = queryset.update(status="Processed")

    modeladmin.message_user(
        request,
        f"{updated_count} order(s) successfully marked as processed.
    )

    @admin.register(Order)
    class OrderAdmin(admin.ModelAdmin):
        list_display = ('id', 'customer', 'status', 'created_at')
        list_filter = ('status', 'created_at')
        actions = [mark_orders_processed]