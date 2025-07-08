from prettytable import PrettyTable

ticket_details = []

def load_data():
    try:
        with open("movies.txt", "r") as file:
            for line in file:
                movie_id, title, price, available_seats = line.strip().split(',')
                ticket_details.append({
                    "id": int(movie_id),  
                    "title": title,
                    "price": int(price),
                    "seats": int(available_seats)
                })
    except FileNotFoundError:
        print("File does not exist")

def add_movie():
    movie_id = int(input("Enter movie ID: "))
    title = input("Enter title of Movie: ")
    price = int(input("Enter Price Of Ticket: "))
    available_seats = int(input("Enter Available Seats: "))

    if any(movie_id == movie["id"] for movie in ticket_details):
        print("ID already exists in the list.")
        return

    data = {
        "id": movie_id,
        "title": title,
        "price": price,
        "seats": available_seats
    }
    ticket_details.append(data)

    t = PrettyTable(['ID', 'Title', 'Price', 'Available Seats'])
    t.add_row([data["id"], data["title"], data["price"], data["seats"]])
    print(t)

def display():
    if not ticket_details:
        print("No tickets available.")
    else:
        t = PrettyTable(['ID', 'Title', 'Price', 'Available Seats'])
        for movie in ticket_details:
            t.add_row([movie['id'], movie['title'], movie['price'], movie['seats']])
        print(t)

def book_ticket():
    cust_name = input("Enter Customer Name: ")
    movie_id = int(input("Enter Movie ID: "))
    no = int(input("Enter number of seats: "))

    found = False
    for movie in ticket_details:
        if movie['id'] == movie_id:
            found = True
            if movie['seats'] >= no:
                movie['seats'] -= no
                save_booking(cust_name, movie_id, no)
                print(f"Thank you {cust_name} for booking {no} tickets for movie ID {movie_id}")
            else:
                print("Not enough seats available.")
            break

    if not found:
        print("Movie ID not found.")

def save_booking(cust_name, movie_id, no):
    with open("tickets.txt", "a") as f:
        f.write(f"Customer Name: {cust_name}, No of booked Tickets: {no}, Movie ID: {movie_id}\n")
    print("Saved booking successfully.")

def delete_ticket():
    movie_id = int(input("Enter movie ID to delete: "))
    found = False
    for movie in ticket_details:
        if movie['id'] == movie_id:
            ticket_details.remove(movie)
            found = True
            print(f"Movie ID {movie_id} deleted successfully.")
            break

    if not found:
        print("Movie ID not found in list.")

load_data()

while True:
    print("\nMenu:")
    print("1. Add Movie")
    print("2. Display Movies")
    print("3. Book Ticket")
    print("4. Delete Movie")
    print("5. Exit")

    try:
        ch = int(input("Enter Choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if ch == 1:
        add_movie()
    elif ch == 2:
        display()
    elif ch == 3:
        book_ticket()
    elif ch == 4:
        delete_ticket()
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid Choice")
