from django.urls import path
from .views import create_payment, confirm_payment

urlpatterns = [
    path('create/<int : order_id>', create_payment, name='create_payment'),
    path('confirm/<int: order_id>', confirm_payment, name='confirm_payment'),
]