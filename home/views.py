from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .serializers import ItemSerializer

class CreateUserReview(generics.CreateAPIView):
    serializer_class = UserReviewSerializer
    permission_classes = [permissions.IsAutenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuItemReviewListView(generics.ListAPIView):
    serializer_class = UserReviewSerializer

    def get_queryset(self):
        menu_item_id = self.kwargs.get("menu_item_id")
        return UserReview.objects.filter(menu_item_id=menu_item_id)
        