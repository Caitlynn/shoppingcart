from service import ProductService


class IpadDiscountWhenPurchaseOver4:
    def __init__(self, shopping_cart):
        self.shopping_cart = shopping_cart

    def apply_rule(self):
        ipad = ProductService().get_product('ipd')
        ipad_count = self.shopping_cart.products.count(ipad)
        if ipad_count > 4:
            self.shopping_cart.total -= ipad_count * (ipad.price - 499.99)

        return self.shopping_cart
