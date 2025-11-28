from datetime import datetime
from .models import DailyOperatingHours
from orders.utils import calculate_tip_amount

def get_today_operating_hours():
    current_day = datetime.today().strftime('%A')

    try:
        today_hours = DailyOperatingHours.objects.get(day=current_day)
        return today_hours.open_time, today_hours.close_time
    except DailyOperatingHours.DoesNotExist:
        return None,None

calculate_tip_amount(100,15)
calculate_tip_amount(250.75,10)