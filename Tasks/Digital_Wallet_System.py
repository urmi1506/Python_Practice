class WalletUser:
    total_users = 0
    total_wallet_balance = 0

    def __init__(self, user_id, name, balance=0):
        self.user_id = user_id
        self.name = name
        self.balance = balance
        self.transaction_history = []

        WalletUser.total_users += 1
        WalletUser.total_wallet_balance += balance

    def add_money(self, amount):
        if amount <= 0:
            print(f" Invalid amount: {amount}")
            return

        self.balance += amount
        WalletUser.total_wallet_balance += amount
        self.transaction_history.append(f"Added Rs {amount}")
        print(f" Rs {amount} added to {self.name}. New balance: Rs {self.balance}")

    def spend_money(self, amount):
        if amount <= 0:
            print(f" Invalid amount: {amount}")
            return

        if self.balance < amount:
            print(" Transaction failed: Insufficient balance")
            return

        self.balance -= amount
        WalletUser.total_wallet_balance -= amount
        self.transaction_history.append(f"Spent Rs {amount}")
        print(f" Rs {amount} spent. Remaining balance: Rs {self.balance}")

    def transfer_money(self, amount, other_user):
        if amount <= 0:
            print(f" Invalid amount: {amount}")
            return

        if self.balance < amount:
            print(" Transfer failed: Insufficient balance")
            return

        self.balance -= amount
        other_user.balance += amount

        self.transaction_history.append(f"Transferred Rs {amount} to {other_user.name}")
        other_user.transaction_history.append(f"Received Rs {amount} from {self.name}")
        print(f" Rs {amount} transferred from {self.name} to {other_user.name}")

    def view_transaction_history(self):
        if not self.transaction_history:
            print(f"No transactions for {self.name} yet.")
            return

        print(f"Transaction History for {self.name}:")
        for txn in self.transaction_history:
            print(" -", txn)

    @classmethod
    def display_details(cls):
        print(f"Total Wallet Users: {cls.total_users}")
        print(f"Total Money in System: Rs {cls.total_wallet_balance}")

    
