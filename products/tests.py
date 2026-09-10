from django.contrib.auth.models import User
from django.test import TestCase

from accounts.models import SellerProfile
from store.models import Store

from .models import Product


class HomePageTests(TestCase):
    def test_home_page_displays_active_products(self):
        seller = User.objects.create_user(username="seller")
        seller_profile = SellerProfile.objects.create(user=seller)
        store = Store.objects.create(seller=seller_profile, name="Test Store")
        active_product = Product.objects.create(
            store=store,
            name="Active Product",
            price="100.00",
        )
        Product.objects.create(
            store=store,
            name="Inactive Product",
            price="200.00",
            is_active=False,
        )

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/home.html")
        self.assertContains(response, active_product.name)
        self.assertNotContains(response, "Inactive Product")
