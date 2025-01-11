l=[1,2,3,4,5,6,7]
for i in l :
    print(i)
print()

# ----- #
for i in 'hey' :
    print(i)
print()

# ----- #
l1=[[1,2,3,4],5.6,6+8j,7]
for i in l1 :
      print(type(i))
print()

# ---- #
for i in l1 :
    if type(i)==int :
      print((i))
    elif type(i) == list :
        for j in i:
            if type(j) == int:
                print(j)
print()

#print ind of all the element
l=[2,45,78,12,"sudh",6+7j,[56,67,78,"dsfdsf"]]
l_len=len(l)
for i in range (l_len) :
    print("index",i,"for an element", l[i])
print()

#Following code give string from list
for i in range(l_len):
    if isinstance(l[i], str): 
        print(l[i])
print()

#Extract all the list of char if element is string
for i in l:
    if type(i) == str:
        l1=[]
        for j in i :
            l1.append(j)
            #print(l1)..if we write print here its consider part of inner loop & print op acc to it
        print(l1)
print()

#Enumerate : in-buit function which return tuples of index and its element
for i in enumerate(l):
    print(i)
print()

# in following code its give index and element in seperate format
for i,j in enumerate(l):
    print(i , j)
print()

#return a list after doing a square of all the int element
for i in l:
    if type(i) == int:
        l2=[]
        l2.append(i**2)
        print(l2)


