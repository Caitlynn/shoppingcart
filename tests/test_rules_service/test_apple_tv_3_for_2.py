import unittest

from model import ShoppingCart
from service import ShoppingCartService, ProductService


class AppleTv3For2TestCase(unittest.TestCase):
    def setUp(self):
        self.apple_tv = ProductService().get_product('atv')
        self.apple_tv_price = self.apple_tv.price

    def test_apple_tv_3_for_2_discount(self):
        test_cart = ShoppingCart()
        test_cart_service = ShoppingCartService(test_cart)

        test_cart_service.scan(self.apple_tv)
        test_cart_service.scan(self.apple_tv)
        test_cart_service.scan(self.apple_tv)

        assert test_cart_service.checkout() == self.apple_tv_price * 2


if __name__ == '__main__':
    unittest.main()
