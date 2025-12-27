import string
import secrets
from .models import Coupon 
from decimal import Decimal, InvalidOperation
from django.db.models import Sum
from .models import Order

def calculate_discount(order_total, discount_percentage):
    try:
        order_total = Decimal(order_total)
        discount_percentage = Decimal(discount_percentage)

        if order_total < 0 or discount_percentage < 0:
            raise ValueError("Value must be non-negetive")

            discount_amount = order_total * (discount_percentage / decimal("100"))
            return discount_amount.quantize(Decimal("0.01"))

        except (InvalidOperation, TypeError):
            raise ValueError("Invalid input: order_total and discount_percentage must be numeric")
            
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