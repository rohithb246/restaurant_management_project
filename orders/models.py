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
        
