import string
import secrets
from .models import Coupon 
from decimal import Decimal
from django.db.models import Sum
from .models import Order


def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits

while True:
    code = ''.join(secrets.choice(characters) for _ in range(length))
    
    if not Coupon.objects.filter(code-code).exists():
        return code

def generate_unique_order_id(length=8):
    characters = string.ascii_uppercase + string.digits

    while True:
        order_id = ''.join(secrets.choice(characters) for _ in range(length))

        if not Order.objects.filter(order_id=order_id).exist():
            return order_id

def get_daily_sales_total(date):
    sales_data = Order.objects.filter(created_at_date=date).aggregate(total_sum=Sum('total_price'))
    total = sales_data['total_sum']
    return total if total is not None else Decimal('0.00')