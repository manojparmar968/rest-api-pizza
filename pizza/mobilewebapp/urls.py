from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mobilewebapp.views import *

router = DefaultRouter()
router.register(r'v1/order', OrderViewSet, basename='OrderViewSet')


urlpatterns = [
    path('', include(router.urls)),
]
