class Order:
    def __init__(self, id, items, customer):
        self.id = id
        self.items = items
        self.customer = customer


class OrderValidator:
    def validate(self, order):
        print("Walidacja zamówienia.")


class OrderDatabaseSaver:
    def save_to_database(self, order):
        print("Zapisywanie zamówienia do bazy danych.")


class OrderEmailSender:
    def send_confirmation_email(self, order):
        print("Wysyłanie e-maila potwierdzającego.")


class OrderProcessor:
    def __init__(self, order, validator, saver, email_sender):
        self.order = order
        self.validator = validator
        self.saver = saver
        self.email_sender = email_sender

    def process_order(self):
        self.validator.validate(self.order)
        self.saver.save_to_database(self.order)
        self.email_sender.send_confirmation_email(self.order)


# Przykład użycia:
order = Order("123", ["Produkt A", "Produkt B"], "Jan Kowalski")
validator = OrderValidator()
saver = OrderDatabaseSaver()
email_sender = OrderEmailSender()

processor = OrderProcessor(order, validator, saver, email_sender)
processor.process_order()
