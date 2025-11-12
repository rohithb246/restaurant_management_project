from rest_framework import serializers
from .models import MenuItem
from .models import Ingredient
from .models import Table
from django.db import models
from .models import MenuItem

class MenuIteSerializer(serializers.modelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name','description', 'price' ]

class IngredientSerializer(serializers.modelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class TableSerializer(serializers.modelSerializer):
    class  Meta:
        model = Table
        field = '__all__'
