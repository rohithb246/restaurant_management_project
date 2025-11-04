from django.db import models
from django.utils import timezone

class Coupon(models,Model):
      code = models.CharField(max_length=50, unique=True)
      discount_percentage = models.DecimalField(max_digit= 5, decimal_places=2)
      is_active = models.BooleanField(default=True)
      valid_from = models.DateField()
      valid_until = models.DateField()

      def _str_(self):
        return self.code
        
