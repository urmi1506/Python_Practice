# Tuples
t1=(1,"urmi",3+1j,4.55)
# access data
print(t1[0:2])
# reverse order
print(t1[::-1])
# type
print(type(t1))

# List
l1=[1,"urmi",3+1j,4.55]
# access data
print(l1[0:2])
# reverse order
print(l1[::-1])
# type
print(type(l1))

l2=[2,'urmila',9.89]
print(l1+l2)
print(l1*2)

# print(l1+'urmi')# give err bcz diff datatypes
print(l1+['urmi'])
# list is mutable and in string its not possible .string is immutable
l1[0]='urmila'
print(l1)

print(len(l1))
print ('urmi' in l1)

l2.append('hey') 
print (l2)

l2.append([2,3,4])
print(l2)

l2.extend([7,8,9])
print(l2)

l1.pop() #by default index for pop is -1 ..last ele
print(l1)

l2.insert(1,'hello')
print (l2)

l2.insert(0,[1,2,3,4])
print(l2[0][3])

l2.reverse()
print(l2)

print(l2.count('urmila'))


