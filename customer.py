from shopping_cart import ShoppingCart

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()

    def add_product(self,product):
        self.cart.add_product(product)

    def view_cart(self):
        for product in self.cart.product_list:
            print(product.name)
