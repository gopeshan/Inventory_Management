class CreditDebitCard:
    def __init__(self, card_number, card_holder, expiration_date, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.cvv = cvv

    def __str__(self):
        return f"Card Number: {self.card_number}, Card Holder: {self.card_holder}, Expiration Date: {self.expiration_date}, CVV: {self.cvv}"
        
class Payment:
    def __init__(self, amount, payment_method, card=None):
        self.amount = amount
        self.payment_method = payment_method
        self.card = card