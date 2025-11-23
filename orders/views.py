from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from .models import Order
from .serializers import OrderSerializer
from .serializers import PaymentMethodSerializer

class OrderDetailAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'

    @action(detail=True, methods=['delete'], url_path="cancel")
    def cancel_order(self, request, pk=None):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Respose(
                {"error": "order not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        if request.user.customer != order.customer:
            return Respose(
                {"error": "you are allowed to cancel this order."},
                status=status.HTTP_403_FORBIDDEN
            )
        
        order.status = 'Cancelled'
        order.save()

        return Respose(
            {"message": "Order successfully cancelled."},
            status=status,HTTP_200_OK
        )

class PaymentMethodListView(ListAPIView):
    serializer_class = PaymentMethodSerializer

    def get_queryset(self):
        return PaymentMethod.objects.filter(is_active=True)