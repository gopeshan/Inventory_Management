class Order:
    def __init__(self, customer, product, quantity):
        self.customer = customer
        self.product = product
        self.quantity = quantity
    
    def validate_order(self):
        if self.quantity > 0 and self.quantity <= self.product.quantity:
            return True
        else:
            print("Invalid order quantity.")
            return False
