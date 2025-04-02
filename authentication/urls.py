from django.urls import include, path
from rest_framework import routers
from .views import loginView
from rest_framework.routers import DefaultRouter
from .views import UserInfo
router= DefaultRouter()
router.register(r'auth', UserInfo, basename='auth')
urlpatterns = [
    path('', include(router.urls)),
    path('login/', loginView.as_view(), name='login'),]