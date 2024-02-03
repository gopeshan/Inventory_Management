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
        print(f"Product added to {self.name}, name, price, quantity)}")

    def add_customer(self, name, email):
        self.cursor("INSERT INTO customers (name, email) VALUES (?, ?)",
                            (name, email))
        self.connection.commit()
        print(f"Customer added to {self.name} store: {Customer(self.cursor, name, email)}")
