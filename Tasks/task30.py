details = {}
seat_info = {}
book_info = {}
train_book = {}
while True:

    print("---Railway Reservation System---")
    print("1. Add Passenger")
    print("2. Check Seat Availability")
    print("3. Book a Seat")
    print("4. Cancel Booking")
    print("5. Show All Bookings")
    print("6. Exit")

    ch=int(input("Enter Choice:"))

    match(ch):
        case(1):
            names=input("Enter Name:")
            age=int(input("Enter Age:"))
            train=input("Enter Train Name:")
            details["name"]=names
            details["age"]=age
            details["train"]=train
            print("Passenger added successfully.")
        case(2):
             train_name=input("Enter Train Name:")
             total_seats=int(input("Enter total seats:"))
             book_seats=int(input("Enter book seats:"))
             seat_info[train_name]=total_seats
             book_info[train_name]=book_seats

             available=total_seats - book_seats
             print(f"Seats Available :{available}")

        case(3):
            train=input("Enter train name :")
            if train in seat_info and train in book_info:
                available = seat_info[train] - book_info[train]
                if(available >0):
                   name=input("Enter Name:")
                   age=int(input("Enter age:"))
                
                   train_book['name']=name
                   train_book['age']=age
                   train_book['train']=train

                   book_info[train] += 1
                   print("Booking Added")
                else:
                   print("No Seat Available")
        case(4):
            name=input("Enter passanger name:")
            if name in train_book:
                train = train_book[name]["train"]
                book_info[train] -= 1
                del train_book[name]
                print("Booking cancelled.")
            else:
                print("Booking not found.")
        case(5):
            print("all bookings:")
            for name, info in train_book.items():
                print(f"Name: {name}, Age: {info['age']}, Train: {info['train']}")
        case 6:
            print("Exit.")
            break

        case _:
            print("Invalid Choice.")





    
    

    