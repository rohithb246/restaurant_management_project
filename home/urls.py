from django.urls import path
from .views import ItemListCreateView, ItemDetailView

urlpatterns = [
   path('categories/', MenuCategoryListView.as_view(),name='menu-categories'),
]
