from django.db import models
from django.db.models import Count

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        verbase_name = "Menu Category"
        verbase_name_plural = "Menu Categories"

        def __str__(self):
            return self.name

class NutritionalInformation(models.Model):
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE, related_name='nutritional_info')
    calories = models.IntegerField()
    protein_grams = models.DecimalField(max_digits=5, decimal_places=2)
    fat_grams = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrate_grams = models.DecimalField(max_digits=5, decimal_places=2)

class DailySpecialManager(models.Manager):
    def upcoming(self):
        today = datetime.date.today()
        return self.filter(date__gte=today)

class DailySpecial(models.Model):
    name =  models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()

    objects = DailySpecialManager()

class MenuItemManager(models.Manager):
    def get_top_selling_items(self, num_items=5):
        return (
            self.get_queryset()
            .annotate(total_orders=Count('orderitemss'))
            .order_by('total_orders')[:num_items]
        )

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_daily_special = models.BooleanField(default=False)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    objects = MenuItemManager()


    def _str_(self):
        return self.name

    def get_final_price(self):
        if self.discount_percentage > 0:
            discount_amount = (self.price * self.discount_percentage) / 100
            return float(self.price - discount_amount)
        return float(self.price)

class Category(models.Model):
    Category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.Category_name

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='menu_items')
    is_available = models.BooleanField(default=True)

    def __str__(self)
    return self.name

class LoyaltyProgram(models.Model):
    name = models.CharField(max_length=50, unique=True)
    points_required = models.IntegerField(unique=True)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    operating_days = models.CharField(
        max_length=100,
        help_text="Comma-separated days (e.g., Mon,Tue,Wed,Thu,Fri,)"
    )

    def __str__(self):
        return self.name

class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"