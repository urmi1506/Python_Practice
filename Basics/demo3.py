# String
str="urmi"
print(str)
# access indexes
print(str[0])
# access character in backword direction
print(str[-1])

# acess ch in range
print(str[0:3])

# print (str[10])...for individual give err
print (str[0:10])

print (str[-1:-3]) #conflict bw + & - dire bcz default jump size 1

# start:end:jump_size...size default 1
print (str[0:10:2])  

print(str[0:10:-1])  #give blank bcz of conflict of dire
print (str[-1:-3:-1])

print(str[::])
# by default start pt:0 ,end pt:len of str 

print (str[-1:]) #give data bcz there in no conflict
  
print(str[::-1])

# repeat
s="urmi"
print(s*3)

# concate
s1="urmi" + "1506"
print(s1)

# len
print(len(s1))

# access ind or ch
print(str[0])

print(str.find('i'))

# count
print(str.count('i'))

# split
s2="I am the best"
print(s2.split())
print(s2.split('t'))

# upper
print(s2.upper())

# swapcase
s3="Urmi"
print(s3.swapcase())

# title
print(s1.title())
print(s1.capitalize())

# join
print("_".join("urmi"))

# reverse
for i in reversed("urmi"):
  print(i)

# strip..remove space
s4=" Urmi "
print(s4.strip())
print(s4.rstrip())
print(s4.lstrip())

# replace...str immutable nd here its change the address so its able to replace
print(s4.replace('m','v'))

# expandtab
s5="urmi\tbest"
print(s5.expandtabs())

# whole string must statisfy cond otherwise its give u false
print(s5.isupper())
print(s5.islower())
print(s5.isspace())
print(s5.isdigit())
print(s5.endswith('t'))
print(s5.startswith('u'))
print(s5.istitle())






