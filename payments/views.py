import stripe
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from orders.models import Order

# Set the Stripe API Key
stripe.api_key = settings.STRIPE['SECRET_KEY'] 

@api_view(['POST'])
def create_payment(request):
    try:
        order_id = request.data.get("order_id")  # Extract order ID from request
        if not order_id:
            return Response({"error": "Order ID is required"}, status=400)

        order = Order.objects.get(id=order_id, user=request.user, status='pending')
        amount = int(order.total_price * 100)  # Convert to cents

        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='usd',
            payment_method_types=['card'],
        )

        return Response({"client_secret": payment_intent["client_secret"]})
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@api_view(["POST"])
def confirm_payment(request):
    try:
        order_id = request.data.get("order_id")
        if not order_id:
            return Response({"error": "Order ID is required"}, status=400)

        order = Order.objects.get(id=order_id, user=request.user, status="pending")
        order.status = "paid"
        order.save()

        return Response({"message": "Payment successful"})
    except Order.DoesNotExist:
        return Response({"error": "Order not found"}, status=404)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
