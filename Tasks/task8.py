# Random Password Generator using given string

import random
import json #used to store & transfer data

len = int (input("Enter Length of Password :"))
print(len)


final_list = "abcdefghijklmnopqrstuvwxyz123456789!@#$%^&*()_+-=`~"


password = []

for i in range(len):
    randompass = random.choice(final_list)
    password.append(randompass)
 

final_pass = "".join(password)
print(final_pass)

dict = {
    "passkey" :final_pass
}
# serialization req to convert python object into json format
json_object = json.dumps(dict)    #used when Python objects have to be stored in file nd f is file pointer

with open('data.json', 'w') as f:
     f.write(json_object)