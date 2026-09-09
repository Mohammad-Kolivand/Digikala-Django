from django.shortcuts import render

from .models import Product

def home(request):
    products = (
        Product.objects
        .filter(is_active=True)
        .select_related("store")
        .order_by("-created_at")
    )

    return render(
        request,
        "products/home.html",
        {"products": products},
    )