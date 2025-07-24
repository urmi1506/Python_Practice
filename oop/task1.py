
class Student:
    
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        self.total=sum(marks.values())
        self.avg=self.total/len(marks)
        self.grade=self.cal_grade()

    def cal_grade(self):
        if self.avg >= 90:
            return 'A'
        elif self.avg >= 75:
            return 'B'
        elif self.avg >= 60:
            return 'C'
        elif self.avg >= 40:
            return 'D'
        else:
            return 'F'
    
    def display(self):
        print(f"Name:{self.name}")
        print(f"Roll No:{self.roll_no}")
        for subject,mark in self.marks.items():
            print(f"{subject}:{mark}")
        print(f"Total:{self.total},Average:{self.avg:.2f},Grade:{self.grade}")

stud_rec=[]

def add_stud():
    name=input("Enter Name:")
    try:
        roll_no=int(input("Enter Roll No:"))
    except ValueError:
        print("Invalid numeric value is entered")

    for s in stud_rec:
        if s.roll_no==roll_no:
            print("Roll No Already Exist")
            return
    
    marks={}
    for i in range(3):
        subject=input("Enter subject name:")
        mark=int(input(f"Enter marks for {subject}:"))
        marks[subject]=mark

    stud=Student(name,roll_no,marks)
    stud_rec.append(stud)
    print("Student added Successfully")

def display_all():
    if not stud_rec:
        print("No Student display")
    else:
        for s in stud_rec:
            s.display()

def search():
    roll_no=int(input("Enter roll no to search:"))
    for s in stud_rec:
        if s.roll_no==roll_no:
            s.display()
            return
    print("Student Not found")

def update():
    roll_no=int(input("Enter roll no to search:"))
    for s in stud_rec:
        if s.roll_no==roll_no:
            marks={}
            for i in range(3):
                subject=input("Enter subject name:")
                mark=int(input(f"Enter marks for {subject}:"))
                marks[subject]=mark
            s.marks=marks
            s.total = sum(marks.values())
            s.avg=s.total / len(marks)
            s.grade = s.cal_grade()
            print("Record Updated")
            return
    print("Student not found")

def delete():
    roll_no=int(input("Enter roll no to delete:"))
    for i in range(len(stud_rec)):
        if stud_rec[i].roll_no==roll_no:
            del stud_rec[i]
            print("Record deleted")
            return
    print("Student not found")

def main():
    while True:
        print("1. Add New Student")
        print("2. Display All Students")
        print("3. Search by Roll Number")
        print("4. Update Student Record")
        print("5. Delete Student Record")
        print("6. Exit")
        try:
            choice=int(input("Enter Choice:"))
        except ValueError:
            print("Invalid numeric valid entered")


        if choice == 1:
            add_stud()
        elif choice == 2:
            display_all()
        elif choice == 3:
            search()
        elif choice == 4:
            update()
        elif choice == 5:
            delete()
        elif choice == 6:
            print("Exiting..")
            break
        else:
            print("Invalid choice is entered")

main()
        