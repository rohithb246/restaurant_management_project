from rest_framework import serializers
from .models import MenuItem
from .models import Ingredient
from .models import Table
from django.db import models
from .model import UserReview
from .models import MenuItem
from .models import MenuCategory
from .model import Restaurant, DailyOperatingHours

class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fiels = ['id', 'user', 'rating', 'text', 'created_at']

class DailySpecialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        field = ['id', 'name', 'price', 'description']
        
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name','description', 'price','category' ]
    
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
        
class MenuItemSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name','image']

class MenuItemDetailSerializer(serializer.ModelSerializer):
    category = serializer.StringRelatedField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = MenuItem
        fields = [
            "id",
            "name",
            "category",
            "price",
            "image",
            "is_available",
            "category",
        ]

    def get_image(self, obj):
        request = self.content.get("request")
        if obj.image and request:
            return request.build_absolute.uri(obj.image.url)
        return None