from django.urls import path
from .views import create_payment, confirm_payment  # Correctly imported

urlpatterns = [
    path('create-payment/', create_payment),  # No need to prefix with `views`
    path('confirm-payment/', confirm_payment),
]
