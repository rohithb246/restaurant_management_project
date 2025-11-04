from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
        from .models import OrderStatus
        from . import PENDING,PROCESSING,COMPLETE,CANCELLED

        default_statuses = [PENDING,PROCESSING,COMPLETE,CANCELLED]
    
    for status in default_statuses:
        OrderStatus.objects.get_or_create(name=status)