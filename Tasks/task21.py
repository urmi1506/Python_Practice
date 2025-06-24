
name =input("Enter Name :")
age =int(input("Enter Age :"))
height =float(input("Enter Height in cm :"))
meter = height / 100.0

print(f"Hello {name} ,you are {age} years old , your height is {meter} meters ." )

if(age >= 18):
    print(f"Driving Licence : Yes")
else:
    print(f"Driving Licence : No ")



