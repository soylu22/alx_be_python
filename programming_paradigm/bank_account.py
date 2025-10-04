# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        # Encapsulated attribute
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display current account balance."""
        print(f"Current Balance: ${self.__account_balance:.2f}")

