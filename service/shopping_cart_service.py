from service.rules_service.apple_tv_3_for_2 import AppleTv3For2
from service.rules_service.free_vga_per_macbook_pro import FreeVgAPerMacbookPro
from service.rules_service.ipad_discount_when_purchase_over_4 import IpadDiscountWhenPurchaseOver4


class ShoppingCartService:
    def __init__(self, shopping_cart=None):
        self.shopping_cart = shopping_cart if shopping_cart is None else shopping_cart

    def scan(self, product):
        self.shopping_cart.products.append(product)

    def remove_product(self, product):
        self.shopping_cart.products.remove(product)

    def total(self):
        return self.shopping_cart.total

    def checkout(self):
        for product in self.shopping_cart.products:
            self.shopping_cart.total += product.price

        # apply discount
        self.shopping_cart = AppleTv3For2(self.shopping_cart).apply_rule()
        self.shopping_cart = IpadDiscountWhenPurchaseOver4(self.shopping_cart).apply_rule()
        self.shopping_cart = FreeVgAPerMacbookPro(self.shopping_cart).apply_rule()

        return self.shopping_cart.total
