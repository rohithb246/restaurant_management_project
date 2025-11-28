from rest_framework import generics
from .models import Item
from .serializers import ItemSerializer

# List and Create API for all items
class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer