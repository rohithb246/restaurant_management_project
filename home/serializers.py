from rest_framework import serializers
from .models import MenuItem
from .models import Ingredient
from .models import Table
from django.db import models
from .model import UserReview
from .models import MenuItem
from .models import MenuCategory

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fiels = ['id', 'user', 'rating', 'text', 'created_at']

class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        field = ['id', 'name', 'price', 'description']
        
class MenuIteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name','description', 'price' ]
    
    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.validationError("Rating must be betweeen 1 and 5")
        return value
        
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

class DailyOperatingHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyOperatingHours
        fields = ['day', 'open_time', 'close_time']
        