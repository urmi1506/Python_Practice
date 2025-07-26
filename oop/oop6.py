# default argument sol for method overloading
class Emp:
    def __init__(self,name,age=0,sal=0.0):
        self.name=name
        self.age=age
        self.sal=sal

e1=Emp("amit")
e2=Emp("Sumit",23)
e3=Emp("Anit",30,50000.)
print(e1.name)
print(e2.name,e2.age)
print(e3.name,e3.age,e3.sal)        