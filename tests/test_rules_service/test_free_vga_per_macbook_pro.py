import unittest

from model import ShoppingCart
from service import ProductService, ShoppingCartService


class FreeVgAPerMacbookProTestCase(unittest.TestCase):
    def setUp(self):
        self.vga_adapter = ProductService().get_product('vga')
        self.macbook_pro = ProductService().get_product('mbp')
        self.macbook_pro_price = self.macbook_pro.price

    def test_free_vga_with_each_macbook_pro_purchase(self):
        test_cart = ShoppingCart()
        test_cart_service = ShoppingCartService(test_cart)

        test_cart_service.scan(self.macbook_pro)
        test_cart_service.scan(self.macbook_pro)
        test_cart_service.scan(self.vga_adapter)

        assert test_cart_service.checkout() == self.macbook_pro_price * 2


if __name__ == '__main__':
    unittest.main()
