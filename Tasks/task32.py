from prettytable import PrettyTable
import datetime


data=[]

while True:
    print("--- Grocery Billing System ---")
    print("1. Add Item")
    print("2. View Bill")
    print("3. Generate Receipt")
    print("4. Exit")

    try:
        ch= int(input("Enter Choice :"))
    except ValueError:
        print("Invalid integer choice")

    match(ch):
        case(1):
            items=input("Enter Item Name :")
            quantity=int(input("Enter Quantity of Item :"))
            price=float(input("Enter price of item per unit :"))
            total=quantity*price
            
            data.append({
                "Item":items,
                "Qty":quantity,
                "Price":price,
                "Total":total
            })
        
        case(2):
            if not data:
                print("No items in bill yet")
            else:
                print("\n--- Bill Summary ---")
                t=PrettyTable(['Item','Qty','Price','Total']) 
                for item in data:
                    t.add_row([item['Item'], item['Qty'], item['Price'], item['Total']])
                print(t)
                grandTotal=0
                for x in data:
                    grandTotal+=x['Total']
                print(f"Grand Total :{grandTotal}")

        case(3):
            name=input("Enter Name :")
            curr_time=datetime.datetime.now()  #if directly use this give err due to colon 
            time_info = curr_time.strftime("%Y-%m-%d_%H-%M-%S")

            filename = f"receipt_{name}_{time_info}.txt"

            if not data:
                print("No items to generate receipt.")
                continue

            with open(filename, "w") as f:
                f.write(f"Customer Name: {name}\n")
                f.write(f"Date & Time: {time_info}\n")
                f.write("Items:\n")
                for item in data:
                    f.write(f"- {item['Item']} | Qty: {item['Qty']} | Price: {item['Price']} | Total: {item['Total']}\n")

                f.write(f"\nGrand Total: {grandTotal}\n")
                f.write("Thank you\n")

            print(f"Receipt saved as '{filename}'")

        case(4):
            print("Exit")

        case(_):
            print("Invalid Choice")

