# count length of string
s="Hello it's me urmi this side"
len(s)
print()

# other method
cnt=0
for i in s:
    cnt +=1
print(cnt)
print()

# Reverse a string
s1="urmi"
ans=s1[::-1]
print (ans)
print()

for i in range(len(s)-1,-1,-1):
    print(s[i])