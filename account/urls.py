from django.urls import path
from .views import UserProfileViewSet

user_profile = UserProfileViewSet.as_view({
    'put': 'update'
})

urlpatterns = [
    path('profile/update/', user_profile, name='profile-update'),
    
]