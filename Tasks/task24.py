
# stud_name1 = input("Enter a student Name1:")
# stud_name2 = input("Enter a student Name2:")
# stud_name3 = input("Enter a student Name3:")
# stud_name4 = input("Enter a student Name4:")
# stud_name5 = input("Enter a student Name5:")

# stud =[stud_name1 ,stud_name2,stud_name3,stud_name4,stud_name5]

stud=[]
for i in range(5):
    name =input(f"Enter student name {i+1}:")
    stud.append(name)          


unique = set(stud)
print(unique)

l=len(unique)
print(f"Total unique names : {l}")

t =tuple(unique)

print("names in Tuple:")
for i in t:
    print(i)

name=input("Enter name to search :")

flag = False

for ele in  t:
    if ele == name:
       flag = True
       break

if flag:
    print(f"Yes , {name} is in the student list")




