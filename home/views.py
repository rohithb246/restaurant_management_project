from rest_framework.views import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer

# List and Create API for all items
class MenuCategoryListView(ListAPIView):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

class MenuItemSearchViewSet(ViewSet):
    pagination_class = MenuItemSearchPagination

    def list(self, request):
        query = response.GET.get('q', '')
        queryset = MenuItem.objects.all()

        if query:
            queryset = queryset.filter(Q(name_icontains=query))

        pagination = self.pagination_class()
        result_page = pagination.paginate_queryset(queryset, request)
        serializer = MenuItemSerializer(result_page, many=true)
        return paginator.get_paginated_response(serializer.data)