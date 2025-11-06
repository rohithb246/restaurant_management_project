from rest_framework import serializers
from .models import MenuItem

class MenuIteSerializer(serializers.modelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name','description', 'price' ]