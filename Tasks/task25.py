dict ={}
adult={}

for i in range(5):
    name=input("Enter name :")
    age=int(input("Enter Age :"))
    dict[name]=age
    
    if age >= 18 :
      adult[name]=age

print(f"Adult Dictionary :{adult}")

l=[]
for x in adult:
    l.append(x.upper())
    # res = [x.upper()]
print(f"Adult Names (uppercase): {l}")

name=input("Enter name to check :")

flag = False

for ele in  dict:
    if ele == name:
       flag = True
       break

if flag:
    print(f"Yes , {name} is in the list")


