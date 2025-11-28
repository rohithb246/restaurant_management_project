from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.respose import Respose
from rest_framework import status
from .models import Order
from rest_framework.generics import RetrieveAPIView
from .models import Order
from .serializers import OrderSerializer
from .serializers import PaymentMethodSerializer
from rest_framework import status as drf_status

@api_view(['GET'])
def order_status_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist
    return Respose(
        {
            {"detail": "ordernot found"},
            status=drf_status.HTTP_404_NOT_FOUND
            "order_id": order.id,
            "status": order.status
            
        },
        status=status.HTTP_200_OK
    )
    data = {
        "order_id": order_id,
        "status": order.status
    }
    return Respose(data, status=drf_status.HTTP_200_OK)
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

class UpdateOrderStatusView(APIView):
    def put(self, request, order_id):
        try:
            order = Order,objects.get(id=order_id)
        except Order.DoesNotExist:
            return Respose(
                 {"error": "Order not found"},
                 status=status.HTTP_404_NOT_FOUND
            )
        serializer = OrderStatusUpdateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.update(order, serializer.validated_data)
            return Respose(
                {"message": "order status updated successfully"},
                status=status.HTTP_200_OK
            )
            return Respose(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderStatusUpdateView(APIView):
    def post(self, request):
        serializer = OrderStatusSerializer(data=request.data)

        if not serializer.is_valid():
            return Respose(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        order_id = serializer.validated_data['order_id']
        new_status = serializer.validated_data['status']

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Respose(
                {"error": "Invalid order id"},
                status=status.HTTP_404_NOT_FOUND
            )

            order.status = new_status
            order.save()

            return Respose(
                {"message": "order status update successfully"}
                status=status.HTTP_200_OK
            )