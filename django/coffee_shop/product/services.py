from .exceptions import InsuficientStock
from .models import Product


class ProductService:

    def buy_product(self, pk):
        product = Product.objects.get(pk=pk)
        if not product.stock:
            raise InsuficientStock('Product dont have stock.')
        product.stock -= 1
        product.save()
