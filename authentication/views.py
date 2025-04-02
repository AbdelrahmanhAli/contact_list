from django.shortcuts import render
from .models import UserInfo
from .serializers import UserInfoSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
from authentication.models import UserInfo
from django.conf import settings
from django.contrib import auth
from rest_framework.response import Response
from rest_framework import status
import jwt
# Create your views here.
class UserInfo(viewsets.ModelViewSet):
    queryset= UserInfo.objects.all()
    serializer_class=UserInfoSerializer
 
class loginView(generics.GenericAPIView):
    serializer_class = UserInfoSerializer
    def post(self,request):
        data= request.data
        username= data.get('username','')
        password= data.get('password','') 
        user= auth.authenticate(username=username,password=password)
        if user:
            auth_token-jwt.encode({'username':user.username},settings.JWT_SECRET_KEY,algorithm='HS256')
            serializer= UserInfoSerializer(user)
            data={
                'user':serializer.data,
                'token':auth_token,
            }
            return Response(data,status=status.HTTP_200_OK)
        return Response({'error':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)