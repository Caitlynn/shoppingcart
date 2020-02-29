import unittest

from model import ShoppingCart
from service import ProductService, ShoppingCartService


class IpadDiscountWhenPurchaseOver4TestCase(unittest.TestCase):
    def setUp(self):
        self.ipad = ProductService().get_product('ipd')
        self.discount_ipad_price = 499.99

    def test_discount_price_when_purchase_more_than_4_ipads(self):
        test_cart = ShoppingCart()
        test_cart_service = ShoppingCartService(test_cart)

        for i in range(5):
            test_cart_service.scan(self.ipad)

        assert test_cart_service.checkout() == self.discount_ipad_price * 5


if __name__ == '__main__':
    unittest.main()
