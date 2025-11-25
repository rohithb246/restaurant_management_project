from django.urls import path
from .views import ItemListCreateView, ItemDetailView
from .views import MenuItemSearchSet
from .views import MenuItemIngredientsView
from .views import AvailableTablesAPIView
from .views import ContactFormSubmission
from rest_framework.routers import DefaultRouter
from .views import MenuCategoryViewSet
from .views import DailySpecialsView

router = DefaultRouter()
router.register(r'menu-categories', MenuCategoryViewSet, basename='menucategory')

urlpatterns = [
    path('',include(router.urls)),
]

urlpatterns = [
    path('menu-items/search/', MenuItemSearchSet.as_view({'get':'list'}),name='menu-items-search'),
]

urlpatterns = [
   path('categories/', MenuCategoryListView.as_view(),name='menu-categories'),
]

urlpatterns = [
    path('menu-items/<int:pk>/ingredients/' MenuItemIngredientsView.as_view(), name='menu-item-ingredients'),
]

urlpatterns = [
    path('api/tables/available/',AvailableTablesAPIView.as_view(), name='available_tables_api')
]

urlpatterns = [
    path('contact/submit/', ContactFormSubmissionView.as_view(), name='contact-submit'),
]

urlpatterns = [
    path('daily-specials/', DailySpecialsView.as_view(), name='daily-specials')
]