from datetime import datetime
from .models import DailyOperatingHours

def get_today_operating_hours():
    current_day = datetime.today().strftime('%A')

    try:
        today_hours = DailyOperatingHours.objects.get(day=current_day)
        return today_hours.open_time, today_hours.close_time
    except DailyOperatingHours.DoesNotExist:
        return None,None