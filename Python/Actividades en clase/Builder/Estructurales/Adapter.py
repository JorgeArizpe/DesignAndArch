from abc import ABC, abstractmethod

class PayPalService(ABC):
    def pay(self, amount):
        print(f'Payment sent: {amount} to PayPal')

class StripeService:
    def pay(self, amount):
        print(f'Payment made: {amount} to Stripe')

class MercadoPagoService:
    def pay(self, amount):
        print(f'Money sent: {amount} to Mercado Pago')

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class PayPalAdapter(PaymentProcessor):
    def __init__(self, service):
        self.paypal_service = service

    def process_payment(self, amount):
        self.paypal_service.pay(amount)

class StripeAdapter(PaymentProcessor):
    def __init__(self, service):
        self.stripe_service = service
    
    def process_payment(self, amount):
        self.stripe_service.pay(amount)

class MercadoPagoAdapter(PaymentProcessor):
    def __init__(self, service):
        self.mercadoPago_service = service
    
    def process_payment(self, amount):
        self.mercadoPago_service.pay(amount)

def main():
    payment_amount = 100
    
    paypal_processor = PayPalAdapter(PayPalService())
    stripe_processor = StripeAdapter(StripeService())
    mercadoPago_processor = MercadoPagoAdapter(MercadoPagoService())
    
    print('Processing payment with PayPal:')
    paypal_processor.process_payment(payment_amount)
    
    print('\nProcessing payment with Stripe:')
    stripe_processor.process_payment(payment_amount)
    
    print('\nProcessing payment with Mercado Pago:')
    mercadoPago_processor.process_payment(payment_amount)

if __name__ == '__main__':
    main()