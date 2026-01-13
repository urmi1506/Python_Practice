class BankAccount :
    total_account = 0
    total_bank_balance = 0

    def __init__ (self , acc_no , holder_name , acc_type , balance):
        self.acc_no = acc_no 
        self.holder_name = holder_name
        self.acc_type =acc_type.lower()
        self.balance = balance
        self.transaction_hist = []

        BankAccount.total_account +=1
        BankAccount.total_bank_balance +=balance

    def deposit_money(self ,amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return
        
        self.balance += amount
        BankAccount.total_bank_balance += amount
        self.transaction_hist.append(f"Added RS {amount}")
        print(f"RS {amount} deposited successfully")
        print(f"New Balance: {self.balance}")

    def withdrawal_money(self ,amount):
        if amount <= 0:
            print(f"Invalid withdrawal amount")
            return
        
        # saving acc rule
        if self.acc_type == "savings":
            if self.balance - amount <1000:
                print("Withdrawal denied : Minimum balance of Rs 1000 required")
                return
        
        
        if self.balance < amount:
            print("Insufficient balance")
            return
        
        self.balance -= amount
        BankAccount.total_bank_balance -= amount
        self.transaction_hist.append(f"Withdrawn Rs {amount}")

        print(f"{amount} withdrawn successfully")
        print(f"Remaining Balance : Rs {self.balance}")
            
    
    def transfer_money(self,amount,other_users):
        if amount <= 0:
            print(f"Invalid amount:{amount}")
            return
        
        if self.balance < amount :
            print(f"Insufficient fund ,Transfer failed")
            return
        

        self.balance -= amount
        other_users.balance += amount

        self.transaction_hist.append(f"Transferred Rs {amount} to {other_users.holder_name}")
        other_users.transaction_hist.append(f"Received Rs {amount} from {self.holder_name}")
        print(f" Rs {amount} transferred from {self.holder_name} to {other_users.holder_name}")

    def transaction_history(self):
        if not self.transaction_hist:
            print(f"No Transaction for {self.holder_name} yet")
            return
        
        print(f"Transaction history for {self.holder_name}")
        for hist in self.transaction_hist:
            print("~",hist)

    @classmethod
    def display_details(cls):
        print(f"Total Bank Users: {cls.total_account}")
        print(f"Total Money in System: Rs {cls.total_bank_balance}")

acc1 = BankAccount(101, "Urmi", "savings", 5000)
acc2 = BankAccount(102, "Aaru", "Current", 10000)

acc1.deposit_money(1500)
acc1.withdrawal_money(300)
acc1.transfer_money(2000, acc2)

acc1.transaction_history()
acc2.transaction_history()

BankAccount.display_details()

    





