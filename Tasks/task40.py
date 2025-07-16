from datetime import date
import json
import re
filename = "C:\\Python\\Python_Practice\\Tasks\\books.txt"
user_info="C:\\Python\\Python_Practice\\Tasks\\users.txt"
record_info="C:\\Python\\Python_Practice\\Tasks\\borrowed.txt"
books = []
users=[]
borrowed=[]
def load_books():
    try:
        global books
        with open(filename, "r") as f:
            for line in f:
                data = json.loads(line)
                books.append(data)
        merge_books={}

        for book in books:
            # create unique key
            key=(book['title'],book['author'])

            if key in merge_books:
                merge_books[key]+=book['copies']
            else:
                merge_books[key]=book['copies']

        res=[]
        for(title,author),copies in merge_books.items():
            res.append({'title': title, 'author': author, 'copies': copies})
        books = res  
    except FileNotFoundError:
        print("File not found.")

def load_users():
    try:
        with open (user_info,"r")as f:
            for line in f:
                data=json.loads(line)
                users.append(data)
                
    except FileNotFoundError:
        print("File Not Found")

def load_borrow():
    try:
        with open (record_info,"r")as f:
            for line in f:
                data=json.loads(line)
                borrowed.append(data)

    except FileNotFoundError:
        print("File Not Found")


def add_book():
    title=input("Enter Book Title:")
    author=input("Enter Author Name:")
    try:
        copies=int(input("Enter No of Available Copies:"))
    except ValueError:
        print("Invalid numeric no is entered.")
        return

    for book in books:
        if book['title']==title and book['author']==author:
            book['copies']+=copies
            break
    else:
      add={
        'title':title,
        'author':author,
        'copies':copies
         }
      books.append(add)

    with open (filename,"w") as f:
        for book in books:
           f.write(json.dumps(book)+"\n")
    

def reg_user():
    name=input("Enter User Name:")
    contact=input("Enter contact:")
    if not re.match(r'[\w\.-]+@[\w\.-]+\.\w+$',contact):
        print("Invalid Contact entered")
        return

    rec={
        'name':name,
        'contact':contact
    }
    users.append(rec)
    save_data()

def save_data():
    try:
        with open(user_info,"w")as f:
            for item in users:
                f.write(json.dumps(item)+"\n")
    except FileNotFoundError:
        print("File Does not found")


def borrow_book():
    user=input("Enter User Name:")
    title=input("Enter Title of Book:")
        
    for item in books:
        if item['title']==title and item['copies'] >= 1:
            item['copies'] -=1
            borrowed_date=str(date.today())
            add_borrow_book(user,title,borrowed_date)
            save_borrow()

    
def add_borrow_book(user,title,borrowed_date):
        new_data={
            'user':user,
            'book':title,
            'borrow_date':borrowed_date
        }
        borrowed.append(new_data)

def save_borrow():
    with open(record_info,"w")as f:
        for item in borrowed:
            f.write(json.dumps(item)+"\n")

def return_book():
    user=input("Enter User Name:")
    title=input("Enter Title of Book:")
    for items in borrowed[:]:
        if items['book']==title and items['user']==user and 'borrow_date' in items:

            for item in books:
                if item['title'] == title:
                   item['copies']+=1
                   break
            borrowed.remove(items)
            return_date= str(date.today())
            add_return_book(user,title,return_date)
            save_borrow()
    
def add_return_book(user,title,return_date):
    return_data={
            'user':user,
            'book':title,
            'return_date':return_date
        }
    borrowed.append(return_data)

def view_borrowed_books():
    try:
        with open(record_info,"r")as f:
            for line in f:
                data=json.loads(line)
                if 'borrow_date' in data:
                    print(f"User: {data['user']}, Book: {data['book']}, Borrowed: {data['borrow_date']}")

    except FileNotFoundError:
         print("File Not Found")

def all_data():
    load_books()
    load_users()
    load_borrow()
all_data()   


while True:
    print("1.Add Books")
    print("2.Register User")
    print("3.Borrow Book")
    print("4.Return Book")
    print("5. View Borrowed Books")
    print("6. Exit")

    try:
       ch=int(input("Enter Choice:"))
    except ValueError:
        print("invalid numeric no is entered")
    if ch==1:
        add_book()
    elif ch==2:
        reg_user()
    elif ch==3:
        borrow_book()
    elif ch==4:
        return_book()
    elif ch==5:
        view_borrowed_books()
    elif ch==6:
        print("Exit")
        break
    else:
        print("Invalid Choice")
    