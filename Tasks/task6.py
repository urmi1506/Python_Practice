# Random Password Generator

import random
import string

# take length
len =int (input("Length of Your Password :"))
print(len)

print("choose Number to set password : 1.Digits ,2.Characters ,3.Special_character ,4.Exit")
charlist = ""

final_list = "abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()_+-=`~"
while True :
    ch = int (input("Choose Choice :"))

    if ch == 1: charlist+=string.digits
    elif ch == 2: charlist+=string.ascii_letters
    elif ch == 3 : charlist+=string.punctuation
    elif ch == 4 : break
    else : print ("Invalid Choice")

password = []

for i in range(len):
    randompass = random.choice(charlist)
    password.append(randompass)
 

final_pass = "".join(password)
print("Random Password is: " + final_pass)

with open("password.txt", "w") as f:
    f.write(final_pass)