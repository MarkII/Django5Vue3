from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from users.models import Users
from users.serializers import UserRegisterSerializer, UserInfoSerializer, UserUpadateSerializer

class RegisterUserView(APIView):
    
    def post(self, request):    
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    def get(self, request):
        serializer = UserInfoSerializer(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
        
    def put(self, request):
        user_id = request.user.id
        current_user = Users.objects.get(id=user_id)
        serializer = UserUpadateSerializer(current_user, request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)