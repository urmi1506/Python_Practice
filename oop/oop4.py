class Emp:
    def __init__(self,name):
        self.name=name
    def __init__(self,name,age):
        self.name=name
        self.age=age
e=Emp("Urmi")
print("Name:",e.name)
e2=Emp("Urmi",21)
print("Name:",e.name,"Age:",e.age)
        
# the method /function overloading is not possible in python
# Function with different parameter Knbown as function overloading
# not possible in python bcz :
# dynamically typed nd interpreted language, Single function name maps to a single function object in the namespace.

