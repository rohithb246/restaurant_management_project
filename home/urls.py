from django.urls import path
from .views import ItemListCreateView, ItemDetailView
from .views import MenuItemSearchSet

urlpatterns = [
    path('menu-items/search/', MenuItemSearchSet.as_view({'get':'list'}),name='menu-items-search'),
]

urlpatterns = [
   path('categories/', MenuCategoryListView.as_view(),name='menu-categories'),
]
