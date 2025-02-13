from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(title="CartCraze API", default_version="v1", description="CartCraze API",),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/account/", include("account.urls")),  # Make sure this line is correct
    path("api/products/", include("products.urls")),
    path("api/cart/", include("cart.urls")),  # Cart API
    path("api/orders/", include("orders.urls")),  # Orders API
    path("api/payments/", include("payments.urls")),  # Payments API
    path("docs/", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

# Optionally, you can serve static files during development (if enabled in settings)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
