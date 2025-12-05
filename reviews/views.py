from rest_framework.generics import ListAPIView
from .models import Review
from .serializers import ReviewSerializer
from .pagination import ReviewPagination

class ReviewListAPIView(ListAPIView):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination