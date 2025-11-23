from django.test import TestCase
from django.urls import path
from .view import PaymentMethodListView

urlpatterns = [
    path('payment-methods/', PaymentMethodListView.as_view(), name='payment-method-list'),
]