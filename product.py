class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.id}, Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"
