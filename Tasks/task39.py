from prettytable import PrettyTable
details=[]
order_details=[]
def load_data():
    try:       
        with open ("menu.txt","r")as f:            
            for line in f:                
                item,price=line.strip().split(',')                
                details.append({                    
                    'item':item,
                    'price':float(price)                
                })
    except FileNotFoundError:
        print("File Not Found")

def add_data():
    item=input("Enter Name Of Item:")
    price=float(input("Enter Price :"))
    data={
        'item':item,
        'price':price
    }
    details.append(data)
    save_data()

def save_data():
    with open("menu.txt","w")as f:
        for item in details:
            f.write(f"{item['item']},{item['price']}")

def view_data():
    if not details:
        print("No Data Exist")
    t=PrettyTable(['Item','Price'])
    for item in details:
        t.add_row([item['item'],item['price']])
    print(t)

def order_data():
    cust_name=input("Enter Customer Name:")
    item=input("Enter Item Name:")
    quantity=int(input("Enter quantity:"))

    item_exists = False
    for menu_item in details:
        if menu_item['item'].lower() == item.lower():
            price = menu_item['price']
            item_exists = True
            break

    if not item_exists:
        print("Item Not Exist")
        return
    
    order={
        'customer':cust_name,
        'item':item,
        'quantity':quantity,
        'price':price
    }
    order_details.append(order)
    
    
def cal_bill():
    t = PrettyTable(['Customer', 'Item', 'Quantity', 'Unit Price', 'Total'])
    grandtotal=0
    for item in order_details:
        total=item['quantity']*item['price']
        grandtotal+=total
        t.add_row([item['customer'], item['item'], item['quantity'], f"{item['price']:.2f}", f"{total:.2f}"])
    print(t)
    print(f"Total = {grandtotal}")

def save_order():
    with open ("orders.txt","a")as f:
        for order in order_details:
            f.write(f"{order['customer']}|{order['item']}:{order['quantity']}\n")

def save_bills():
    with open ("bills.txt","a")as f:
      for order in order_details:
            total = order['quantity'] * order['price']
            f.write(f"{order['customer']}|{order['item']}:{order['quantity']} = {total:.2f}\n") 
        
from prettytable import PrettyTable

def view_order():
    if not order_details:
        print("No orders have been placed yet.")
        return

    t = PrettyTable(['Customer', 'Item', 'Quantity'])

    for order in order_details:
        customer = order['customer']
        for order in order_details:
            t.add_row([order['customer'], order['item'], order['quantity']])

    print("\nAll Orders:")
    print(t)

def menu():
    load_data()  
    while True:
        print("\n--- Restaurant Management System ---")
        print("1. View Menu")
        print("2. Add Menu Item")
        print("3. Place Order")
        print("4. View All Orders")
        print("5. View Bill")
        print("6. Save Orders")
        print("7. Save Bills")
        print("8. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_data()
        elif choice == '2':
            add_data()
        elif choice == '3':
            order_data()
        elif choice == '4':
            view_order()
        elif choice == '5':
            cal_bill()
        elif choice == '6':
            save_order()
        elif choice == '7':
            save_bills()
        elif choice == '8':
            print("Exiting..")
        else:
            print("Invalid choice entered")
