from rest_framework import serializers
from .models import MenuItem
from .models import Ingredient
from .models import Table

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