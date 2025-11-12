from django.test import TestCase
from django.urls import path
from . import views

urlspattern = [
    path('api/table/', views.TableListView.as_view(), name'table-list'),

    path('api/table/<int::pk>/', views.TableDetailView.as_view(), name='table-detais'),
]