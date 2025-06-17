# range - generate a data range(low_bound , upp_bound , jump_size)...it execlude upper_bound nd by default jump size is 1
l=list(range(0,6))
print(l)

print(list(range(0,5,3)))

print(list(range(3,10,-1)))

print(list(range(10,6,-1)))

for i in range(7):
    print(i)
print()

# end append something at end of line
n=5
for i in range (0,n):
 for j in range (0,i+1):
    print("hey" ,end="")
 print("\r\r\r")
 


