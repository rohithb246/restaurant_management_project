from django.db import models

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