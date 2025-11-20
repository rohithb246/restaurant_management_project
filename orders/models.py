from django.db import models
from .models import OrderStatus
from decimal import Decimal
from account.models import Customer
from home.models import MenuItem
from .utils import generate_unique_order_id

class OrderStatus(models.Model):
    name = models.charField(max_length=50)

    def __str__(self):
        return self.name

class PaymentMethod(models.Model):
    name = models.charField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
         
class Order(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
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

     def calculate_total(self):
        total = Decimal('0.00')
        for item in self.orderitem_set.all()
            total += item.price * item.quantity

        return total

class ActiveOrderManager(models.Manager):
    def get_active_orders(self):
        return self.filter(status__in=['pending', 'processing'])

class OrderItem(models.model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.name} x {self.quantity}"

class order(model.Model):
    order_id = models.charField(max_length=20, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.order_id:
            self.order_id = generate_unique_order_id()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.order_id
        