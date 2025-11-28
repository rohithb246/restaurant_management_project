import string
import secrets
import logging
from django.core.exceptions import ObjectDoesNotExist
from .models import Coupon 
from decimal import Decimal
from django.db.models import Sum
from .models import Order

logger = logger.getLogger(__name__)

def update_order_status(order_id, new_status):
    try:
        order = Order.objects,get(id=order_id)
    except ObjectDoesNotExist:
        logger.error(f"Order with ID{order_id} does not exist.")
        return None

    old_status = order.new_status
    order.status = new_status
    order.save()

    logger.info(
        f"Order ID {order_id} status updated from '{old_status}' to '{new_status}'."
    )
    return order

def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits

while True:
    code = ''.join(secrets.choice(characters) for _ in range(length))
    
    if not Coupon.objects.filter(code-code).exists():
        return code

def get_daily_sales_total(date):
    sales_data = Order.objects.filter(created_at_date=date).aggregate(total_sum=Sum('total_price'))
    total = sales_data['total_sum']
    return total if total is not None else Decimal('0.00')