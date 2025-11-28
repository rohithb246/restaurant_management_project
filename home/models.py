from django.db import models
from django.contrib.auth.models import User
from .models import MenuItem
from django.db import models
from datetime import timedelta

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    customer_name = models.CharField(max_length=200)
    Reservation_time = models.DateTimeField()
    duration = models.DurationField(default=timedelta(hours=1))

    @classmethod
    def find_available_slots(cls, start, end, slot_duration=timedelta(hours=1)):
        reservation = cls.objects.filter(
            reservation_time__lt=end,
            reservation_time__gte=start
        )

        slots = []
        slot = start

        while slot + slot_duration <= end:
            if not reservations.filter(reservation_time__range=(slot, slot_duration)).exists():
                slots.append(slot)
            slot += slot_duration

        return slots

class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    MenuItem = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'menu_item')
        ordering = ['-review_date']

        def __str__(self):
            return f"{self.user.username} - {self.menu_item.name} ({self.rating}/5)"
class LoyaltyProgram(models.Model):
    name = models.CharField(max_length=100, unique=True)
    points_per_dollar_spent = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    is_featured = models.BooleanField(default=false)


class Restaurant(models,Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    has_delivery = models.BooleanField(default=False)

class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)

    @staticmethod 
    def get_random_special():
        specials = DailySpecial.objects.all()
        if specials.exists():
            return specials.order_by(?).first()
        return None
        
def __str__(self):
        return self.name