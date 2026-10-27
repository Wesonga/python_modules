
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        # Validate the initial balance
        if isinstance(initial_balance, bool) or not isinstance(
            initial_balance, (int, float)
        ):
            raise TypeError("Initial balance must be a number.")

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")

        self.owner = owner
        self.__balance = initial_balance
        self.transaction_history = []

        if initial_balance > 0:
            self.transaction_history.append(
                f"Opening deposit: KSh {initial_balance}"
            )

    def deposit(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            print("Error: Deposit amount must be a number.")
            return

        if amount <= 0:
            print("Error: Deposit amount must be positive.")
            return

        self.__balance += amount
        self.transaction_history.append(
            f"Deposit: +KSh {amount}"
        )
        print(f"Successfully deposited KSh {amount}.")

    def withdraw(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            print("Error: Withdrawal amount must be a number.")
            return

        if amount <= 0:
            print("Error: Withdrawal amount must be positive.")
            return

        if amount > self.__balance:
            print("Error: Insufficient funds.")
            return

        self.__balance -= amount
        self.transaction_history.append(
            f"Withdrawal: -KSh {amount}"
        )
        print(f"Successfully withdrew KSh {amount}.")

    def get_balance(self):
        return self.__balance

    def show_transaction_history(self):
        print(f"\nTransaction history for {self.owner}:")

        if not self.transaction_history:
            print("No transactions yet.")
            return

        for number, transaction in enumerate(
            self.transaction_history, start=1
        ):
            print(f"{number}. {transaction}")


# Test the BankAccount class
account = BankAccount("Brian", 5000)

print(f"Account owner: {account.owner}")
print(f"Initial balance: KSh {account.get_balance()}")

account.deposit(2000)
account.withdraw(1500)
account.withdraw(10000)  # Should fail: insufficient funds

print(f"Current balance: KSh {account.get_balance()}")

account.show_transaction_history()
