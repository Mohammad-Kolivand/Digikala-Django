from django.shortcuts import render,get_object_or_404

from .models import Store


def store_list(request):
    stores = (
        Store.objects
        .filter(is_active=True)
        .order_by("name")
    )

    return render(
        request,
        "store/store_list.html",
        {"stores": stores},
    )

def store_detail(request, store_id):
    store = get_object_or_404(
        Store,
        id=store_id,
        is_active=True,
    )
    products = store.products.filter(is_active=True).order_by("-created_at")

    return render(
        request,
        "store/store_detail.html",
        {
            "store": store,
            "products": products,
        },
    )