# Function 

# whn i dont want to write anything under function use pass
def test() :
    pass

# -----if we use print under fuction its an none type so we not able to concate with others
def test1() :
    print ("I am Winner")
test1()

# ----

print(type(test1()))

# a= test1()
# a + "sudh"

# ----

def test2():
    return "this is my first function"
print(test2())

print(type(test2()))

print(test2() + "sudh")

# ----

def test3():
    return 1234

print(type(test3()))

# ---

def test4():
    return 4,3,"sudh",[1,2,3,4,5]
print(test4())

# access data ...approach 1
x=test4()

a,b,c,d = x[0] , x[1] , x[2] , x [3]

print("\n",a,"\n",b,"\n",c,"\n",d)

# access data ...approach 2

p,q,r,s= test4()
print(p,q,r,s)

# ----
def test5():
    a=6*7 /6
    return a
print(test5())

# ----
l = [1,2,3 ,"urmi" ,[4,5,6,7]]

def test6(a):
    n= []
    if type(a) == list :
       for i in a :
           if type(i) == int :
              n.append(i)
    return(n ) #if we use print give u none here

print(test6(l))  

#---
def test7(d):
    

