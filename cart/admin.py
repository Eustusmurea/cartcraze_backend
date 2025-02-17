from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):  # Displays CartItems inside Cart
    model = CartItem
    extra = 1  # Shows an extra empty row for adding items

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    search_fields = ("user__email", "id")
    list_per_page = 20
    inlines = [CartItemInline]  # Allows managing CartItems inside Cart

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ("cart", "product", "quantity", "price")
    list_filter = ("cart",)
    search_fields = ("cart__id", "product__name")