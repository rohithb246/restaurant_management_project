from django.shortcuts import render
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenicated
from rest_framework.response import Response

from .serializers import UserUpdateSerializer

class  UserProfileViewSet(viewsets.Viewset):
    permission_classes = [IsAuthenicated]

    def update(self, request):
        user = request.User
        serializer = UserUpdateSerializer(user, data=request.data)

        if serializer.is_vaild():
            serializer.save()
            return Response({
                "message": "profile updated successfully"
                "data": serializer.data
            }), status=status.HTTP_200_OK

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)