import string
import secrets
from .models import Coupon 

def generate_coupon_code(lenght=10):
    characters = string.ascii_uppercase + string.digits

while True:
    code = ''.join(secrets.choice(characters) for _ in range(lenght))
    
    if not Coupon.objects.filter(code-code).exists():
        return code