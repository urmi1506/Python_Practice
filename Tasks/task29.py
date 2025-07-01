data={}

for i in range(3):
    name=input("\nEnter name :")
    bal=int(input("Enter Amount :"))
    data[name]=bal

print(data)

username=input("Enter username :")
if username in data:
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        ch=int(input("Enter Choice:"))
        match(ch):
            case 1:
                print(f"Balance: Rs.{data[username]}")
            case 2:
                amount = int(input("Enter amount to deposit: "))
                if amount > 0:
                    data[username] += amount
                    print(f"Deposit amount Rs.{amount}. Updated Balance: Rs.{data[username]}")
                else:
                    print("Enter a valid amount.")
            case 3:
                amount = int(input("Enter amount to withdraw: "))
                if 0 < amount <= data[username]:
                    data[username] -= amount
                    print(f"Withdrew Rs.{amount}. Final Balance: Rs.{data[username]}")
                else:
                    print("Invalid or insufficient balance.")
            case 4:
                print("Thank you!")
                break
            case _:
                print("Invalid choice.")
else:
    print("User not found.")
      
     
       

