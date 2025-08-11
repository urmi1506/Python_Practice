class BankAccount:
    def __init__(self,account_number,holder_name,balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def deposit(self ,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive number.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient amount")
    
    @classmethod
    def from_string(cls, account_str):
        account_number, holder_name, balance = account_str.split(',')
        return cls(account_number, holder_name, float(balance))
    
acc1 = BankAccount.from_string("101,John,5000")
print(acc1)
print(acc1.__dict__)
acc1.deposit(3000)
acc1.withdraw(2000)

