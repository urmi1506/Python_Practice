book_details = []
def load_books():
    try:
        with open('books.txt', 'r') as file:
            for line in file:
                book_id, title, author, price, stock = line.strip().split(',')
                book_details.append({
                    'id': book_id,
                    'title': title,
                    'author': author,
                    'price': int(price),
                    'stock': int(stock)
                })
    except FileNotFoundError:
        print("No existing book inventory found")
load_books()

def add_book():
    book_id = input("Enter book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    try:
        price = int(input("Enter book price: "))
        stock = int(input("Enter book stock: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for price and stock.")
        return
    
    data = {
        'id': book_id,
        'title': title,
        'author': author,
        'price': price,
        'stock': stock
    }
    
    book_details.append(data)
def save_books():
    with open('books.txt', 'w') as file:
        for book in book_details:
            file.write(f"{book['id']},{book['title']},{book['author']},{book['price']},{book['stock']}\n")  
def display_books():
    if not book_details:
        print("No books available in the inventory.")
    else:
        print("Available Books:")
        for book in book_details:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Price: {book['price']}, Stock: {book['stock']}")
            
def purchase_books():

    cust_name = input("Enter your name: ")
    try:
        book_id = input("Enter the book ID you want to purchase: ")
        quantity = int(input("Enter the quantity you want to purchase: "))
    except ValueError:
        print("Invalid input. Please enter a valid book ID and quantity.")
        return
    if not book_details:
        print("No books available for purchase.")
        return
    for book in book_details:
        if book['id'] == book_id:
            if book['stock'] >= quantity:
                total_price = book['price'] * quantity
                book['stock'] -= quantity
                print(f"Thank you {cust_name}! You have purchased {quantity} copies of '{book['title']}' for a total of {total_price}.")
                save_bill(cust_name, book_id, quantity, total_price)

                return
            else:
                print(f"Insufficient stock for '{book['title']}'. Available stock: {book['stock']}")
                return
    print(f"No book found with ID {book_id}. Please check the ID and try again.")
def save_bill(cust_name, book_id, quantity, total_price):
    with open('bill.txt', 'a') as file:
        file.write(f"Customer Name: {cust_name}, Book ID: {book_id}, Quantity: {quantity}, Total Price: {total_price}\n")
    print("Bill saved successfully.")
    
def search_book():
    search_title = input("Enter the book title to search: ")
    found_books = [book for book in book_details if search_title.lower() in book['title'].lower()]
    if found_books:
        print("Search Results:")
        for book in found_books:
            print(f"ID: {book['id']}, Title: {book['title']}, Author: {book['author']}, Price: {book['price']}, Stock: {book['stock']}")
    else:
        print("No books found with that title.")

def delete_book():
    book_id = input("Enter the book ID to delete: ")
    for book in book_details:
        if book['id'] == book_id:
            book_details.remove(book)
            save_books()
            print(f"Book with ID {book_id} has been deleted from the inventory.")
            return
    print(f"No book found with ID {book_id}.")
    
while True:
    print("1. Add New Book to Inventory")
    print("2.Display Available Books")
    print("3. Purchase Books ")
    print("4.Search Book by Title")
    print("5. Delete Book from Inventory")
    print("6. Exit and Save")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_book()
        save_books()
        print("Book added successfully.")       
    elif choice == '2':
        display_books()
    elif choice == '3': 
        purchase_books()
        save_books()
        print("Purchase completed successfully.")
    elif choice == '4':
        search_book()  
        print("Search completed successfully.")     
    elif choice == '5':
        delete_book()
        print("Book deleted successfully.")
    elif choice == '6':
        print("Exiting the program and saving changes.")
        break