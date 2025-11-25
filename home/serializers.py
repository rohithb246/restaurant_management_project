from rest_framework import serializers
from .models import MenuItem
from .models import Ingredient
from .models import Table
from django.db import models
from .models import MenuItem
from .models import MenuCategory

class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        field = ['id', 'name', 'price', 'description']
        
class MenuIteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name','description', 'price' ]
class MenuCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuCategory
        fields = ['id','name']
        read_only_fields = ['id']
        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']

class TableSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Table
        field = '__all__'

class ContactFormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactFormSubmission
        fields = ['id', 'name', 'email', 'message']