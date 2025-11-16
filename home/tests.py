from django.test import TestCase
from django.urls import path
from . import views
from rest_framework.test import APITestCase
from rest_framework import status
from home.models import Restaurant

urlspattern = [
    path('api/table/', views.TableListView.as_view(), name'table-list'),

    path('api/table/<int::pk>/', views.TableDetailView.as_view(), name='table-detais'),
]

class RestaurantInfoAPITest(APITestCase):
    def test_get_restaurant_info(self):
        restaurant = Restaurant.objects.create(
            name = "Test Restaurant",
            address = "123 Test St"
        )

        response = self.client.get('/api/restaurant-info/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertIn('name', response.data)
        self.assertIn('address', response.data)

        self.assertEqual(response.data['name'], restaurant.name)
        self.assertEqual(response.data['address'], restaurant.address)
        