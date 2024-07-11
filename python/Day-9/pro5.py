class BankAccount:
    def __init__(self, bank_holder_name, total_amount):
        self.bank_holder_name = bank_holder_name
        self.total_amount = total_amount

    def display_details(self):
        print(f"Bank holder's name: {self.bank_holder_name}")
        print(f"Total amount: ${self.total_amount}")

account = BankAccount("Raj", 4000)
account.display_details()
