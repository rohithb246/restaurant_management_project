from rest_framework import serializers
from .models import MenuItem
from .models import Ingredient

class MenuIteSerializer(serializers.modelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name','description', 'price' ]

class IngredientSerializer(serializers.modelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']