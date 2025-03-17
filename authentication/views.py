from django.shortcuts import render
from .models import UserInfo
from .serializers import UserInfoSerializer
from rest_framework.views import APIView
from rest_framework import viewsets
from authentication.models import UserInfo
# Create your views here.
class UserInfo(viewsets.ModelViewSet):
    queryset= UserInfo.objects.all()
    serializer_class=UserInfoSerializer
 