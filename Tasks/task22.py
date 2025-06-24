
sub1 = float(input("Enter marks of Sub1 :"))
sub2 = float(input("Enter marks of Sub2 :"))
sub3 = float(input("Enter marks of Sub3 :"))
sub4 = float(input("Enter marks of Sub4 :"))
sub5 = float(input("Enter marks of Sub5 :"))

marks = [sub1 , sub2 , sub3 , sub4 , sub5]

total = sum(marks)
avg = total / 5

highest = max(marks)
lowest =min(marks)

print(f"Total :{total}")
print(f"Average :{avg}")
print(f"Highest :{highest}")
print(f"Lowest :{lowest}")
if(sub1 >=35 and sub2>=35 and sub3 >=35 and sub4 >=35 and sub5 >= 35):
    print(f"Result: PASS")
else:
    print(f"Result : Fail")

