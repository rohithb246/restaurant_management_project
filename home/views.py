from rest_framework.views import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
from .serializers import IngredientSerializer
from.models import Table
from.serializers import TableSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.permission import IsAuthenicated
from .models import UserReview
from .serializer import UserReviewSerializer
from .models import ContactFormSubmission
from .serializers import ContactFormSubmissionSerializer
from .serializers import DailySpecialSerializer
from rest_framework.generics import RetrieveAPIView
from .models import Restaurant
from .serializer import RestaurantSerializer
from .models import MenuItem
from .serializers import MenuItemSearchSerializer

@api_view(['GET'])
def search_menu_items(request):
    query = request.GET.get('q','')

    if query:
        items = MenuItem.objects.filter(name_icontains=query)
    else:
        items = MenuItem.objects.none()
    
    serializer = MenuItemSearchSerializer(items, many=True)
    response(serializer.data)

class RestaurantDetailView(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
class DailySpecialSerializer(generics.ListAPIView):
    serializer_class = DailySpecialSerializer

    def get_queryset(self):
        return MenuItem.objects.filter(is_daily_special=True)


class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [IsAuthenicatedOrReadOnly]

class MenuItemSearchViewSet(ViewSet):
    pagination_class = MenuItemSearchPagination

    def list(self, request):
        query = response.GET.get('q', '')
        queryset = MenuItem.objects.all()

        if query:
            queryset = queryset.filter(Q(name_icontains=query))

        pagination = self.pagination_class()
        result_page = pagination.paginate_queryset(queryset, request)
        serializer = MenuItemSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

class MenuItemSearchViewSet(viewsets.ViewSet):
    def update(self, request, pk=None):
        try:
            menu_item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({"error":"Menu items not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MenuItemSerializer(menu_item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.error, status=status.HTTP_400_BAD_RESPONSE)

class MenuItemIngredientsView(RetrieveAPIView):
    def get(self, request, pk):
        try:
            menu_item = MenuItem.objects.get(pk=pk)
        except MenuItem.DoesNotExist:
            return Response({"error":"menu items not found"}, status=status.HTTP_404_NOT_FOUND)

            Ingredients = menu_item.ingredients.all()
            serializer = IngredientSerializer(ingredients, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class TableDetailView(generics.RetrieveAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class AvailableTablesAPIView(APIView):
    def get(self, request):
        available_tables = Table.objects.filter(is_available=True)
        serializer = TableSerializer(available_tables, many=True)
        return Response(serializer.data)

class ContactFormSubmissionView(CreateAPIView):
    queryset = ContactFormSubmission.objects.all()
    serializer_class = ContactFormSubmissionSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "You message has been submitted successfully."},
                status=status.HTTP_201_CREATED
            )

            return Response(
                {"errors": serializer.errors},
                status=status.HTTP_400_BAD_RESPONSE
            )
class UserReviewCreateView(CreateAPIView):
    queryset = UserReview.objects.all()
    serializer_class = UserReviewSerializer
    permission_classes = [IsAuthenicated]