from django.db import models
from .models import OrderStatus

class OrderStatus(models.Model):
    name = models.charField(max_length=50)

    def __str__(self):
        return self.name
 
class Order(models.Model):
    status = models.ForeignKey(
        'OrderStatus',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def _str_(self):
        return f"Order #{self.id} - {self.status.name if self.status else 'No status'}"

    def get_unique_item_names(self):
        items_names = {item.menu_item.name for item in self.orderitem_set.all()}
        return list(item_names)
        
class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__in=['pending', 'processing'])
        