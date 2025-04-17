# Random Password Generator using given string

import random
import string

len = int (input("Enter Length of Password :"))
print(len)


final_list = "abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()_+-=`~"


password = []

for i in range(len):
    randompass = random.choice(final_list)
    password.append(randompass)
 

final_pass = "".join(password)
print("Random Password is: " + final_pass)

with open("res.txt", "w") as f:
    f.write(final_pass)
