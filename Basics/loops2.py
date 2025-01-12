l=["name","emailid","phoneno","address"]
for i in l:
    print(i+"...hey")
print()

#------#
s="hey"
for i in s:
    print(i)
print()

#---for-else statement---#
for i in l:
    print(i)
else:
    print("if for loop completely executed then and then it will run this ")
print()

#--------#
for i in l:
    if i == "emailid":
        break
    print(i)
else:
    print("otherwise executed this")
print()
for i in l:
    if i == "name":
        break
else:
    print("otherwise executed this")
print()

#----While loops----#
a=1
while a < 6 :
    print(a)
    a+=1
print()

b=1
while b< 5:
    print(b)
    if b == 4 :
        break
    b +=1
print()

# c=1
# while c< 5:
#     print(c)
#     if c == 3 :
#         continue ...(infinite loop issue created due to contine statement)
#     c +=1
# print()

c=1
while c< 5:
    print(c)
    c +=1
    if c == 3 :
        continue 
print()