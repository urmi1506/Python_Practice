from prettytable import PrettyTable

inventory_info = []
filename = "Python_Practice\\Tasks\\invetory_data.txt"

def load_data():
    try:
        with open(filename, "r") as f:
            for line in f:
                id, name, price, quantity = line.strip().split(',')
                inventory_info.append({
                    'id': int(id),
                    'name': name,
                    'price': float(price),
                    'quantity': int(quantity)
                })
    except FileNotFoundError:
        print("File Not Found")

def add_data():
    id = int(input("Enter Product ID: "))
    name = input("Enter Product name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    data = {
        'id': id,
        'name': name,
        'price': price,
        'quantity': quantity
    }
    inventory_info.append(data)
    save_data()

def save_data():
    with open(filename, "w") as f:
        for item in inventory_info:
            f.write(f"{item['id']},{item['name']},{item['price']},{item['quantity']}\n")

def display():
    if not inventory_info:
        print("No data to display.")
        return
    t = PrettyTable(['ID', 'Product Name', 'Price', 'Quantity'])
    for item in inventory_info:
        t.add_row([item['id'], item['name'], item['price'], item['quantity']])
    print(t)

def search():
    id = int(input("Enter Product ID to search: "))
    found = False
    for item in inventory_info:
        if id == item['id']:
            print(f"Product Found: ID = {item['id']}, Name = {item['name']}, Price = {item['price']}, Quantity = {item['quantity']}")
            found = True
            break
    if not found:
        print("ID not present")

def update():
    id = int(input("Enter Product ID to update quantity: "))
    new_qty = int(input("Enter new quantity: "))
    found = False
    for item in inventory_info:
        if id == item['id']:
            item['quantity'] += new_qty
            found = True
            save_data()
            break
    if not found:
        print("ID not present")

def delete():
    id = int(input("Enter Product ID to delete: "))
    found = False
    for item in inventory_info:
        if id == item['id']:
            inventory_info.remove(item)
            found = True
            print(f"Product with ID {item['id']} deleted successfully")
            save_data()
            break
    if not found:
        print("ID not present")

load_data()

while True:
    print("\nMenu")
    print("1. Add a new product")
    print("2. Display all products")
    print("3. Search for a product by ID")
    print("4. Update product quantity")
    print("5. Delete a product")
    print("6. Exit the program")

    try:
        ch = int(input("Enter Choice: "))
    except ValueError:
        print("Invalid choice entered")
        continue

    if ch == 1:
        add_data()
    elif ch == 2:
        display()
    elif ch == 3:
        search()
    elif ch == 4:
        update()
    elif ch == 5:
        delete()
    elif ch == 6:
        print("Exiting..")
        break
    else:
        print("Invalid choice")
