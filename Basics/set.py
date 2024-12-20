l1= [1,2,3,4,5,2,3,4]
# set remove all duplicate element
set(l1)
s={}
print(type(s))
s2={1,2,3,4,4,5,5}
print(type(s2))
print(s2)
# print(s2[0])...give err bcz its unorder collection 

ans=list(s2)
print(ans)
print(s2.add('urmi'))
print(s2)

# res=s2.add([1,2,3])
# print(res)..sets only contain hashable (immutable) types,list is unhashable

res=s2.add((1,2,3,3,4))
print(s2)

s2.remove(4)
print(s2)

s2.discard(3)
print(s2)

# s2.remove(35)
# print(s2)

s2.discard(35)
print(s2)

# sets are case sensitive
s3={'urmi','Urmi'}
print(s3)

