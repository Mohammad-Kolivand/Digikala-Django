from django.shortcuts import render

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