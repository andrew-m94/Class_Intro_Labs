class ShoppingCart:
    def __init__(self):
        self.product_list = []

    def total_price(self):
        total_price = 0
        element = 0
        for product in self.product_list:
            total_price += self.product_list[element].price
            element += 1
            
        return "{:.2f}".format(total_price)
            
    
    def add_product(self,product):
        self.product_list.append(product)

    def clear_cart(self):
        self.product_list = []