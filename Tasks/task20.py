

noOfRecords = int(input("Enter No of student record :"))

studRec = []
for i in range (noOfRecords):
  print(f"\nEnter Student Details : ")
  name = input("Enter Student name : ")
  roll_no = int(input("Enter roll No :"))
  sub1 =float(input("Enter marks of Subject 1 :"))
  sub2 =float(input("Enter marks of Subject 2 :"))
  sub3 =float(input("Enter marks of Subject 3 :"))

  stud = {
    "name" : name,
    "roll_no" : roll_no ,
     "marks"  :{
      "sub1" : sub1 ,
      "sub2" : sub2 ,
      "sub3" : sub3 
    }
  }

  studRec.append(stud)
  avg = (sub1 + sub2 + sub3) /3
# set = ()
s = set()
print("All Student Records : \n")
# for Rec in stud :
#   print(stud) ...going through each data 3 times due to we have 3 key val pair

for rec in studRec:
    # set.add(name)
    s.add(rec['name'])
    print(f"Name: {rec['name']} s.add(rec['name']), Roll No: {rec['roll_no']}, Marks: {rec['marks']}")
    if (avg >= 75) :
       print("Distinction")
    elif (avg >= 60) :
       print("First Class")
    elif (avg >= 50) :
       print("Second Class")
    else :
       print("fail")


# check single space in variable can give u key err here 
print(f"\nunique Students name :" ,s)

d={}

for data in studRec :
   d[roll_no ]= name
print("\nStudent Records (Roll No → Name):")
print(d)
isFound = False
for i in studRec :
   print(f"Enter Roll No :{i['roll_no']}")
   if(isFound == True):
      print(f"Name is:{i['name']}")
   else:
      print(f"Student Not Found")



