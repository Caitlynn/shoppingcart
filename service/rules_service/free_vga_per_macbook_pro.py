from service import ProductService


class FreeVgAPerMacbookPro:
    def __init__(self, shopping_cart):
        self.shopping_cart = shopping_cart

    def apply_rule(self):
        macbook_pro = ProductService().get_product('mbp')
        macbook_pro_count = self.shopping_cart.products.count(macbook_pro)

        vga_adapter = ProductService().get_product('vga')
        vga_count = self.shopping_cart.products.count(vga_adapter)

        if macbook_pro_count >= 1:
            # if vga adapters are already added, apply price discount
            if vga_count >= macbook_pro_count:
                self.shopping_cart.total -= macbook_pro_count * vga_adapter.price
            # if vga adapter numbers are not matching macbook pro numbers, add more
            elif vga_count < macbook_pro_count:
                self.shopping_cart.total -= vga_count * vga_adapter.price
                for _ in range(macbook_pro_count - vga_count):
                    self.shopping_cart.products.append(vga_adapter)
        return self.shopping_cart
