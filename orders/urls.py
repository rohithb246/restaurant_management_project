from django.urls import path
from .views import *
from .views import order_status_view

urlpatterns = [
    
]

urlpatterns = [
    path("orders/<int:order_id>/status/", order_status_view, name="order-status")
]