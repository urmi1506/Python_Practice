class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):                    # Bug 1
        # here its not declare self ..without self its give typer error and we not able to access instance variable
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            # here bug its not use return or else so even balance is insufficient it still proceed to further code which provide wrong ans 
            return
        self.balance -= amount              # Bug 2
        print(f"Withdrawn: {amount}")

    def get_balance(self):
        print(f"Balance: {self.balance}")


acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(1700)
acc.get_balance()

# transferred = acc.balance + 500            # Bug 3
# in bug 3 its only provide new value but not updated original one
acc.deposit(500)                # Updates acc.balance internally
print(f"After transfer: {acc.balance}")
