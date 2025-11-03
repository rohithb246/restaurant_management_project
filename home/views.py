from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

# List and Create API for all items
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Retrieve, Update, and Delete API for a single item
class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
