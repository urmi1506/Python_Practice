t1=(1,"urmi",3+1j,4.55)
t2=(2,"best",5)
print(t1+t2)

print(t1*2)
print(t1.count('u'))
# its not work for specific character
print(t1.index('urmi'))

# nested tuples
t3=('hey',2,('hello',45))
print(t3)

t4=([1,2,'hii'],('hii there',3.5))
print(t4)
print(t4[0][2])

t4[0][2]='hello'
print(t4)

