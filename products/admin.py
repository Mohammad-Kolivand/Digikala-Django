from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "store",
        "category",
        "price",
        "stock",
        "is_active",
    )

    list_filter = (
        "category",
        "store",
        "is_active",
    )

    search_fields = (
        "name",
        "description",
    )