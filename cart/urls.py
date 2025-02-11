from django.urls import path,include
from rest_framework import DefaultRouter
from .views import CartViewset

router = DefaultRouter()
router.register('cart',CartViewset)

urlpatterns = [
    path('',include(router.urls))
]
