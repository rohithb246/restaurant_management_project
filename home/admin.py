from django.contrib import admin

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "has_delivery")
    list_editable = ("has_delivery",)