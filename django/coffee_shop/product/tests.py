from django.test import Client, TestCase
from django.urls import reverse

from .models import Product


class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(description="Café Colônial", price=13.4, stock=5)
        Product.objects.create(description="Café Pelé", price=10, stock=4)

    def tearDown(self):
        Product.objects.all().delete()

    def test_product_to_string(self):
        """Testa a representação em string do produto."""
        p1 = Product.objects.get(description="Café Colônial")
        p2 = Product.objects.get(description="Café Pelé")
        self.assertEqual(str(p1), "Produto (Café Colônial)")
        self.assertEqual(str(p2), "Produto (Café Pelé)")

    def test_buy_and_decrement_stock(self):
        client = Client()

        product = Product.objects.get(description="Café Colônial")
        self.assertEqual(product.stock, 5)

        resp = client.get(reverse('buy', args=[product.id]))

        product = Product.objects.get(description="Café Colônial")
        self.assertEqual(product.stock, 4)
