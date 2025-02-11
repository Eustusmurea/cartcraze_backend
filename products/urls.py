from django.urls import path,include
from rest_framework import DefaultRouter
from .views import ProductViewset

router = DefaultRouter()
router.register('products',ProductViewset)

urlpatterns = [
    path('',include(router.urls))
]