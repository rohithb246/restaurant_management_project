from rest_framework import serializers
from .models import Order, OrderItem
from home.serializers import MenuItemSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()

    class Meta:
        model = OrderItem
        fields = ['menu_item', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'created_at', 'total_price', 'items']
    
class PaymentMethod(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class OrderstatusUpdateSerializer(serializers.Serializer):
    status = serializers.ChoiceField(choice=[c[0] for c in Order.STATUS_CHOICES])

    def update(self, instance, validated_data):
        instance.status = validated_data['status']
        instance.save()
        return instance