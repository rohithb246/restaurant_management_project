from django.db import models
from .models import OrderStatus
 
class Order(models.Model):
    status = models.ForeignKey(
        'OrderStatus',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def _str_(self):
        return f"Order #{self.id}"
        
