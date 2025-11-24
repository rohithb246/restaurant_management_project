from django.urls import path
from .views import *
from .view import OrderDetailAPIView
from .views import UpdateOrderStatusView

urlpatterns = [
    
]

urlpatterns = [
    path('<int:id>/'OrderDetailAPIView.as_view(), name='order_detail_api')
]

urlpatterns = [
    path('orders/<int:order_id>/update-status/', UpdateOrderStatusView.as_view(), name='update-order-status')
]