import unittest
from unittest import mock

from models import Product
from views import ProductTemplateView


class ProductModelTestCase(unittest.TestCase):

    def setUp(self):
        self.product = Product('Cafe colonial setup', 30, 3)

    def tearDown(self):
        del self.product

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_model_repr(self):
        p = Product('Cafe colonial', 13.87, 5)
        self.assertEqual(str(p), f'Product ({p.description}, {p.price}, {p.stock})')

    def test_price_greater_than_20(self):
        self.assertGreater(self.product.price, 20)


class ProductTemplateViewTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.template_view = ProductTemplateView()

    def test_template_menu(self):
        expected_template = """
        Operação
        =============
        1 - Cadastrar
        2 - Listar
        3 - Sair
        : """
        self.assertEqual(expected_template, self.template_view.template_menu())

    @mock.patch('builtins.input', return_value='1')
    def test_template_insert(self, input_patched):
        instance = Product('', 0, 0)
        self.template_view.template_insert(instance)

        self.assertEqual(instance.description.lower(), '1')
        self.assertEqual(instance.price, 1)
        self.assertEqual(instance.stock, 1)

        self.assertTrue(input_patched.called)
        self.assertEqual(input_patched.call_count, 3)


if __name__ == '__main__':
    unittest.main()
