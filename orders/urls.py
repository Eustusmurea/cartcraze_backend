from django.urls import path,include
from rest_framework import DefaultRouter
from .views import OrderViewset

router = DefaultRouter()
router.register('order',OrderViewset)

urlpatterns = [
    path('',include(router.urls))
]
