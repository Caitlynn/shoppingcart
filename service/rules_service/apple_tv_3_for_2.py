from service import ProductService


class AppleTv3For2:
    def __init__(self, shopping_cart):
        self.shopping_cart = shopping_cart

    def apply_rule(self):
        apple_tv = ProductService().get_product('atv')
        apple_tv_count = self.shopping_cart.products.count(apple_tv)
        if apple_tv_count >= 3:
            # get the number of 3 for 2 sets of apple tv
            sets_applied_discount = (apple_tv_count - apple_tv_count % 3) / 3
            # apply discount to the sets, one apply tv for free in each set
            discount = sets_applied_discount * apple_tv.price
            self.shopping_cart.total -= discount

        return self.shopping_cart
