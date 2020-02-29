import unittest

from model import ShoppingCart
from service import ShoppingCartService, ProductService


class ShoppingCartServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.apple_tv = ProductService().get_product('atv')
        self.ipad = ProductService().get_product('ipd')
        self.vga_adapter = ProductService().get_product('vga')
        self.macbook_pro = ProductService().get_product('mbp')

    def test_apple_tv_discount(self):
        test_cart = ShoppingCart()
        test_cart.service = ShoppingCartService(test_cart)

        test_cart.service.scan(self.apple_tv)
        test_cart.service.scan(self.apple_tv)
        test_cart.service.scan(self.apple_tv)
        test_cart.service.scan(self.vga_adapter)

        assert test_cart.service.checkout() == 249.00

    def test_ipad_discount(self):
        test_cart = ShoppingCart()
        test_cart.service = ShoppingCartService(test_cart)

        test_cart.service.scan(self.apple_tv)
        test_cart.service.scan(self.ipad)
        test_cart.service.scan(self.ipad)
        test_cart.service.scan(self.apple_tv)
        test_cart.service.scan(self.ipad)
        test_cart.service.scan(self.ipad)
        test_cart.service.scan(self.ipad)

        assert test_cart.service.checkout() == 2718.95

    def test_macbook_pro_discount(self):
        test_cart = ShoppingCart()
        test_cart.service = ShoppingCartService(test_cart)

        test_cart.service.scan(self.macbook_pro)
        test_cart.service.scan(self.ipad)
        test_cart.service.scan(self.vga_adapter)

        assert test_cart.service.checkout() == 1949.98


if __name__ == '__main__':
    unittest.main()
