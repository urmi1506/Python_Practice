from prettytable import PrettyTable

students = {
    "Alice": 92,
    "Bob": 74,
    "Charlie": 85
}

def get_grade(marks):
    if marks >= 90:
        return "A"
    elif 75 <= marks <= 89:
        return "B"
    elif 60 <= marks <= 74:
        return "C"
    else:
        return "F"

def print_report(students):
    t = PrettyTable(['Name', 'Marks', 'Grade'])
    
    for name, marks in students.items():
        grade = get_grade(marks)
        t.add_row([name, marks, grade])
    
    print(t)

def get_Topper(students):
    highest_student = max(students, key=students.get)
    highest_marks = students[highest_student]
    
    print(f"Topper: {highest_student} with {highest_marks} marks")


print_report(students)
get_Topper(students)