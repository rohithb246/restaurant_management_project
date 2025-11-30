from django.urls import path, include

urlpatterns = [
    path('api/menu/', include(menu.urls)),
]