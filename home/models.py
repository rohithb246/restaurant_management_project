from django.db import models

class OrderStatus(models.Models):
    name = models.CharField(Max_length=50, unique=True)

    def _str_(self):
        return self.name