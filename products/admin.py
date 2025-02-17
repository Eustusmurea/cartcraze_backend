from django.contrib import admin
from django.utils.html import format_html
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "stock", "image_preview")
    search_fields = ("name", "id")
    list_per_page = 20
    

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />'.format(obj.image.url))
        return "(No image)"
    
    image_preview.short_description = "Image Preview" 
