from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def _str_(self):
        return self.name