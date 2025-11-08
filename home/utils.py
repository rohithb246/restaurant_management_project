from datetime import datetime
from .models import DailyOperatingHours
from orders.utils import calculate_tip_amount
from datetime import datetime,time

def get_today_operating_hours():
    current_day = datetime.today().strftime('%A')

    try:
        today_hours = DailyOperatingHours.objects.get(day=current_day)
        return today_hours.open_time, today_hours.close_time
    except DailyOperatingHours.DoesNotExist:
        return None,None

def is_restaurant_open():
    now = datetime.now()
    current_time = now.time()
    current_weekday = now.weekday()

    opening_time = time(9, 0)
    closing_time = time(22, 0)

    if opening_time <= current_time <= closing_time:
        return True
    else:
        return False

calculate_tip_amount(100,15)
calculate_tip_amount(250.75,10)