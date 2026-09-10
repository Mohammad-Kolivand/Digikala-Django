from django.urls import path

from .views import store_detail, store_list


urlpatterns = [
    path("", store_list, name="store-list"),
    path("<int:store_id>/", store_detail, name="store-detail"),
]