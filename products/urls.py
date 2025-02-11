from django.urls import path, include
from rest_framework.routers import DefaultRouter  # ✅ Correct import
from .views import ProductViewset

router = DefaultRouter()
router.register(r'products', ProductViewset)  # Added r'' for better compatibility

urlpatterns = [
    path('', include(router.urls)),
]
