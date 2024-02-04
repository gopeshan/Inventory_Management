import sqlite3
from product import Product
from customer import Customer
from order import Order
from payment import Payment, CreditDebitCard

class OnlineStore:
    def __init__(self, name):
        self.name = name
        self.connection = sqlite3.connect('online_store.db')
        self.cursor = self.connection.cursor()


    def add_product(self, name, price, quantity):
        self.cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
                            (name, price, quantity))
        self.connection.commit()
        print(f"Product added to {self.name} store: {Product(self.cursor.lastrowid, name, price, quantity)}")

    def add_customer(self, name, email):
        self.cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)",
                            (name, email))
        self.connection.commit()
        print(f"Customer added to {self.name} store: {Customer(self.cursor.lastrowid, name, email)}")


    def place_order(self, customer, product, quantity, payment_method, card=None):
        order = Order(customer, product, quantity)

        if order.validate_order():
            self.cursor.execute("INSERT INTO orders (customer_id, product_id, quantity) VALUES (?, ?, ?)",
                                (order.customer.id, order.product.id, order.quantity))
            self.cursor.execute("UPDATE products SET quantity = quantity - ? WHERE id = ?",
                                (order.quantity, order.product.id))
            self.connection.commit()

            # Process payment
            if payment_method.lower() in ["credit", "debit"]:
                payment = Payment(order.total_cost(), payment_method, card)
                payment.process_payment()

                print(f"Order placed in {self.name} store: {order}")
                print(f"Payment details: {payment}")

            else:
                print("Invalid payment method. Please choose 'Credit' or 'Debit'.")

    def display_products(self):
        self.cursor.execute("SELECT * FROM products")
        products = self.cursor.fetchall()
        print(f"Products in {self.name} store:")
        for product_data in products:
            product = Product(*product_data)
            print(product)
            if product.is_low_stock():
                print(f"Low Stock Alert: {product.name} - Quantity: {product.quantity}")
            print(f"Availability Status: {product.availability_status()}")
