import datetime
from prettytable import PrettyTable

employee_details = []

def load_data():
    try:
        with open("employees.txt", "r") as file:
            for line in file:
                emp_id, emp_name = line.strip().split(',')
                employee_details.append({
                    'id': int(emp_id),
                    'name': emp_name
                })
    except FileNotFoundError:
        print("File Does Not Exist")

def save_data():
    with open("employees.txt", "w") as f:
        for emp in employee_details:
            f.write(f"{emp['id']},{emp['name']}\n")

def add_data():
    emp_id = int(input("Enter Employee ID: "))
    emp_name = input("Enter Employee Name: ")
    data = {
        'id': emp_id,
        'name': emp_name
    }
    employee_details.append(data)
    save_data()
    print("Employee added successfully")

def mark_attendance():
    emp_id = int(input("Enter Employee ID to mark attendance: "))
    status = input("Is the employee present? (Y/N): ").strip().upper()
    date_today = datetime.datetime.now().strftime("%Y-%m-%d")

    for emp in employee_details:
        if emp['id'] == emp_id:
            if status == 'Y':
                status_text = 'Present'
            elif status == 'N':
                status_text = 'Absent'
            else:
                print("Invalid status entered")
                return
            print(f"Attendance marked: {emp['name']} - {status_text}")
            with open("attendance.txt", "a") as f:
                f.write(f"{date_today},{emp['id']},{emp['name']},{status_text}\n")
            return

    print("Employee ID not found")

def view_rec():
    try:
        with open("attendance.txt", "r") as f:
            t = PrettyTable(['Date', 'ID', 'Name', 'Status'])
            for line in f:
                date, emp_id, name, status = line.strip().split(',')
                t.add_row([date, emp_id, name, status])
            print(t)
    except FileNotFoundError:
        print("No attendance records found")

def search():
    emp_id = int(input("Enter Employee ID to search: "))
    found = False
    for emp in employee_details:
        if emp['id'] == emp_id:
            print(f"Employee Found: ID={emp['id']}, Name={emp['name']}")
            found = True
            break
    if not found:
        print("Employee not found")

def delete():
    emp_id = int(input("Enter Employee ID to delete: "))
    found_data = False

    for emp in employee_details:
        if emp['id'] == emp_id:
            employee_details.remove(emp)
            found_data = True
            save_data()
            print("Employee deleted successfully")
            break

    if not found_data:
        print("Employee ID not found.")

load_data()

while True:
    print("Employee Details :")
    print("1.Add Employee data")
    print("2.Mark Attendance")
    print("3.View Attendance")
    print("4.Search Employee")
    print("5.Delete Employee")
    print("6.Exit")

    try:
        ch=int(input("Enter Choice :"))
    except ValueError:
        print("Enter Valid Choice")

    if ch== 1:
        add_data()
    elif ch==2:
        mark_attendance()
    elif ch==3:
        view_rec()
    elif ch==4:
        search()
    elif ch==5:
        delete()
    elif ch==6:
        print("Existing")
    else:
        print("Invalid Choice")
