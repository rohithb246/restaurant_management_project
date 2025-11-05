from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

class MenuItem(models.Model):
    name = models.CharField(max_lenght=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)

    is_featured = models.BooleanField(default=false)

    def _str_(self):
        return self.name