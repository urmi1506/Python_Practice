class BankAccount:
    # -------- Bank level data (shared by all accounts) --------
    total_accounts = 0
    total_money_in_bank = 0

    def __init__(self, acc_no, holder_name, balance):
        self.acc_no = acc_no
        self.holder_name = holder_name
        self.balance = balance
        self.transaction_history = []

        BankAccount.total_accounts += 1
        BankAccount.total_money_in_bank += balance

    def deposit_money(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return

        self.balance += amount
        BankAccount.total_money_in_bank += amount
        self.transaction_history.append(f"Deposited Rs {amount}")

        print(f"{self.holder_name} deposited Rs {amount}")
        print("Balance:", self.balance)

    def transfer_money(self, amount, other_account):
        if amount <= 0:
            print("Invalid transfer amount")
            return

        if self.balance < amount:
            print("Transfer failed: Insufficient balance")
            return

        self.balance -= amount
        other_account.balance += amount

        self.transaction_history.append(
            f"Transferred Rs {amount} to {other_account.holder_name}"
        )
        other_account.transaction_history.append(
            f"Received Rs {amount} from {self.holder_name}"
        )

        print(f"Rs {amount} transferred from {self.holder_name} to {other_account.holder_name}")

    def view_transactions(self):
        print(f"\nTransaction History for {self.holder_name}:")
        if not self.transaction_history:
            print("No transactions yet")
            return

        for txn in self.transaction_history:
            print("-", txn)

    @classmethod
    def bank_summary(cls):
        print("\n--- Bank Summary ---")
        print("Total Accounts:", cls.total_accounts)
        print("Total Money in Bank:", cls.total_money_in_bank)

class SavingsAccount(BankAccount):
    MIN_BALANCE = 1000

    def __init__(self, acc_no, holder_name, balance):
        if balance < SavingsAccount.MIN_BALANCE:
            raise ValueError("Savings Account requires minimum Rs 1000")

        super().__init__(acc_no, holder_name, balance)
        print(f"Savings Account created for {holder_name} with Rs {balance}")

    def withdraw_money(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return

        if self.balance - amount < SavingsAccount.MIN_BALANCE:
            print("Withdrawal denied: Minimum balance rule")
            return

        self.balance -= amount
        BankAccount.total_money_in_bank -= amount
        self.transaction_history.append(f"Withdrawn Rs {amount}")

        print(f"{self.holder_name} withdrew Rs {amount}")
        print("Balance:", self.balance)

class CurrentAccount(BankAccount):
    OVERDRAFT_LIMIT = -5000

    def __init__(self, acc_no, holder_name, balance):
        super().__init__(acc_no, holder_name, balance)
        print(f"Current Account created for {holder_name} with Rs {balance}")

    def withdraw_money(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return

        if self.balance - amount < CurrentAccount.OVERDRAFT_LIMIT:
            print("Withdrawal denied: Overdraft limit exceeded")
            return

        self.balance -= amount
        BankAccount.total_money_in_bank -= amount
        self.transaction_history.append(f"Withdrawn Rs {amount}")

        print(f"{self.holder_name} withdrew Rs {amount}")
        print("Balance:", self.balance)

# Create accounts
urmi = SavingsAccount(101, "Urmi", 5000)
aaru = CurrentAccount(102, "Aaru", 10000)

# Transactions
urmi.deposit_money(1500)
urmi.withdraw_money(6000)

aaru.withdraw_money(14000)
aaru.withdraw_money(2000)  # Should fail

# Transfer
urmi.transfer_money(500, aaru)

# View histories
urmi.view_transactions()
aaru.view_transactions()

# Bank summary
BankAccount.bank_summary()

