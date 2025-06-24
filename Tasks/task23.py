no = int(input(f"Enter No of Subjects :"))
data ={}
for i in range (no):
   name =input(f"Enter Subject Name :")
   marks = float(input(f"Enter marks for {name} :"))
   data[name]=marks

def res(data,no):
   total = sum(data.values()) 
   avg = total /no
   highest=max(data , key =data.get)
   lowest = min(data ,key=data.get)

   print(f"Total : {total}")
   print(f"Average :{avg:.2f}")
   print(f"Highest : {highest} ({data[highest]})")
   print(f"Lowest : {lowest} ({data[lowest]})")

   if all(marks >= 35 for marks in data.values()):
      print("Result: PASS")
   else:
      print("Result: FAIL")

res(data,no)


