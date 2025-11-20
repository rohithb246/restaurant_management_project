from datetime import datetime
from .models import DailyOperatingHours
from orders.utils import calculate_tip_amount
from datetime import datetime,time
import re
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def send_custom_email(recipient_email, subject, message):
    try:
        validate_email(recipient_email)
        send_mail(
            subjects=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient_email],
            failed_silently=False,
        )
        return True

        except ValidationError:
            print("invalid email address:", recipient_email)
            return False

        except BadHeaderError:
            print("invalid header found")
            return False

        except Exception as e:
            print("error sending email:", str(e))
            return False
            
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

def is_valid_Phone_number(phone_number: str) -> bool:
    pattern = r"^\+?\d[\d\s-]{8,14}\d$"

    return bool(re.match(pattern, phone_number))