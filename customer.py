class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer ID: {self.id}, Name: {self.name}, Email: {self.email}"