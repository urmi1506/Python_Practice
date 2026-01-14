class BankAccount:
    
    total_accounts = 0
    total_money_in_bank =0
    def __init__(self,acc_no,holder_name ,balance ,transaction_hist):
        self.acc_no =acc_no
        self.holder_name =holder_name
        self.balance =balance
        self.transaction_hist = transaction_hist

        BankAccount.total_accounts +=1
        BankAccount.total_money_in_bank +=balance

    def deposit_money(self , amount):
        if amount <= 0:
            print("amount must be positive")
            return
        
        self.balance +=amount
        
    
        