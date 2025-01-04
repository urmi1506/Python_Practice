l=[1,2,3,4,5,6,7]
for i in l :
    print(i)

# ----- #
for i in 'hey' :
    print(i)
# ----- #
l1=[[1,2,3,4],5.6,6+8j,7]
for i in l1 :
      print(type(i))

for i in l1 :
    if type(i)==int :
      print((i))
    elif type(i) == list :
        for j in i:
            if type(j) == int:
                print(j)