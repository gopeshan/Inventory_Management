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

    def process_order(self):
        self.product.quantity -= self.quantity

    def total_cost(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f"Order - Customer: {self.customer.name}, Product: {self.product.name}, Quantity: {self.quantity}, Total Cost: ${self.total_cost():.2f}"
