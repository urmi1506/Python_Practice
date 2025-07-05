from prettytable import PrettyTable
filename="Python_Practice\\Tasks\\inventory.txt"
def load_inventory():
    inventory = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 3:
                product, qty, price = parts
                inventory.append({
                    "Product": product,
                    "Quantity": int(qty),
                    "Price": float(price)
                })
    return inventory
def save_inventory(inventory):
    with open(filename, "w") as f:
        for item in inventory:
            f.write(f"{item['Product']},{item['Quantity']},{item['Price']}\n")

while True:
    print("---- Inventory Tracker ----")
    print("1. View Inventory")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Delete Product")
    print("5. Save & Exit")

    try:
        ch=int(input("Enter Choice :"))
    except ValueError:
        print("Invalid Choice Enter")

    match(ch):
        case(1):
                inventory = load_inventory()
                t=PrettyTable(['Product','Quantity','Price']) 
                for item in inventory:
                    t.add_row([item['Product'], item['Quantity'], item['Price']])
                print(t)

        case(2):
                inventory=load_inventory()
                product=input("Enter Product Name :")
                qty=int(input("Enter Quantiy :"))
                price=float(input("Enter Price per unit :"))

                found = False
                for item in inventory:
                    if item['Product'].lower() == product.lower():
                       found = True
                       print("Product already exists.")
                       break
                if not found:
                     inventory.append({
                        "Product": product,
                        "Quantity": qty,
                        "Price": price
                     })
                     save_inventory(inventory)
                else:
                     print("Product not found")
            
        case(3):
                inventory = load_inventory()
                product = input("Enter Product Name to Update: ")

                for item in inventory:
                    if item['Product'].lower() == product.lower():
                       print(f"Current Quantity: {item['Quantity']}, Price: {item['Price']}")
                       item['Quantity'] = int(input("Enter New Quantity: "))
                       item['Price'] = float(input("Enter New Price per unit: "))
                       save_inventory(inventory)
                       print("Product updated successfully")
                       break
                    else:
                       print("Product not found")
        case(4):
                    inventory = load_inventory()
                    product = input("Enter Product Name to Delete:")
    
                    for item in inventory:
                        if item['Product'].lower() == product.lower():
                            inventory.remove(item)
                            save_inventory(inventory)
                            print("Product deleted Successfully")
                            break
                    else:
                        print("Product not found")
        case(5):
              print("Save and Existing")  

        case(_):
              print("Invalid Choice")
