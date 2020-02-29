from model.product import Product

ALL_PRODUCTS = [
    Product("ipd", "Super iPad", 549.99),
    Product("mbp", "MacBook Pro", 1399.99),
    Product("atv", "Apple TV", 109.50),
    Product("vga", "VGA adapter", 30.00)
]


class ProductService:
    def __init__(self, products=None):
        self.products = ALL_PRODUCTS if products is None else products

    def get_product(self, sku):
        for product in self.products:
            if product.sku == sku:
                return product
        return None
