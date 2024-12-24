# dictionery: must have key val pair
d={}
print (type(d))
# key :val pair
d={'key1':'urmi','key2':123,'3':[1,2,3,4]}
print(d)
# access
print(d['key1'] )

# key as special character and _key not working
d1={.3:['abc','xyz',4,5,6]} #here it consider .as decimal
print(d1)

d2={'key1':{1,2,3,4}}
print(d2)

d3={'key1':'abcd','key2':1234,'key1':[1,2,3,4,5]}
print(d3['key1']) #store only updated val..that why create unique key each time

# key as special character & _key not working but under string its work 
d4={'@':12}
print(d4)

d5={'name':'urmi' ,'mob_no':12345,'mail':'abc@gmail.com','key1':[1,2,3],'key2':(1,3,5),'key3':{4,5,6}}
print(d5)

print(type(d5['key2']))
print(type(d5['key2'][1]))

print(d5.keys())
print(d5.values())
print(d5.items())

d5['key4']="hello"
print (d5)

del d5['key4']
print(d5)

del d4
# print(d4)

# d6={[1,2]:'hey'}
# print(d6)

d7={(1,2):'hii'}
print(d7)

print(d5.get('key1'))

d1.update(d2)
print(d1)

# ans=d1+d2
# print(ans)
