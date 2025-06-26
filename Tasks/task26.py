stud = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks1 = int(input("Enter marks for subject 1: "))
    marks2 = int(input("Enter marks for subject 2: "))
    marks3 = int(input("Enter marks for subject 3: "))
    
    stud[name] = [marks1, marks2, marks3]


for name in stud:
    marks = stud[name]
    total = sum(marks)
    avg = total / 3
    if all(m >= 35 for m in marks):
      result = "PASS"
    else:
      result = "FAIL"
    print(f"{name} - Marks: {marks}, Total: {total}, Average: {avg:.2f , Result: {result}}")

highest_total = 0
topper_name = ""

for name in stud:
    total = sum(stud[name])
    if total > highest_total:
        highest_total = total
        topper_name = name

print(f"\nTopper: {topper_name} with total {highest_total}")


all_marks = []
for marks in stud.values():
    all_marks += marks

class_avg = sum(all_marks) / len(all_marks)
print(f"\nClass Average: {class_avg:.2f}")

search = input("\nEnter name to search: ")
if search in stud:
    print(f"{search} marks: {stud[search]}")
else:
    print("Student not found.")

delete = input("\nEnter name to delete: ")
if delete in stud:
    del stud[delete]
    print(f"{delete} deleted.")
else:
    print("Student not found.")

