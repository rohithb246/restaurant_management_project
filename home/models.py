from django.db import models

class MenuCategory(models.Models):
    name = models.CharField(Max_length=100, unique=True)

    def _str_(self):
        return self.name