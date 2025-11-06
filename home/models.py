from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

class NutritionalInformation(models.Model):
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE, related_name='nutritional_info')
    calories = models.IntegerField()
    protein_grams = models.DecimalField(max_digits=5, decimal_places=2)
    fat_grams = models.DecimalField(max_digits=5, decimal_places=2)
    carbohydrate_grams = models.DecimalField(max_digits=5, decimal_places=2)


    def _str_(self):
        return self.name