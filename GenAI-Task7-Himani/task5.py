from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment of {amount}")

class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing UPI payment of {amount}")

if __name__ == "__main__":
    credit_card_payment = CreditCardPayment()
    upi_payment = UPIPayment()

    credit_card_payment.process_payment(1000)
    upi_payment.process_payment(500)