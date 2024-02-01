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
        
    def process_payment(self):
        print(f"Processing payment of ${self.amount:.2f} using {self.payment_method}")
        if self.payment_method.lower() in ["credit", "debit"]:
            print("Payment successfully processed")
            if self.card:
                print("Card details:")
                print(self.card)
            else:
            print("Invalid payment method. Please choose 'Credit' or 'Debit'.")

    def __str__(self):
        return f"Payment - Amount: ${self.amount:.2f}, Method: {self.payment_method}"