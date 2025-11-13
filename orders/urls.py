from django.urls import path
from .views import *
from .view import OrderDetailAPIView

urlpatterns = [
    
]

urlpatterns = [
    path('<int:id>/'OrderDetailAPIView.as_view(), name='order_detail_api')
]