students = [("Alice", 92), 
            ("Bob", 55), 
            ("Charlie", 78), ("Diana", 45)]

def print_stud(students):
    for name , marks in students:
        if marks >= 60 :
           print(f"{name}--> {marks}")
        
        
def get_topper(students):
    top_name, top_marks = students[0]  
    
    for name, marks in students:
        if marks > top_marks:
            top_name, top_marks = name, marks
    
    print(f"\nTopper: {top_name} with {top_marks} marks")


print_stud(students)
get_topper(students)
