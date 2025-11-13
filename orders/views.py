from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .models import Order
from .serializers import OrderSerializer

class OrderDetailAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'