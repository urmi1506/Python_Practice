# we can assign val to instance variable in 4 ways:
# 1.using self within constructor/__init__
# 2.using self within instance method
# 3.using object
# 4.using dict

# ---here dict is variable not an method---#
class Emp:
    def __init__(self):
        self.name="urmi"
        self.age=20

e1=Emp()
print(e1.__dict__)

# ------ #
class Emp:
    def __init__(self):
        self.name="urmi"
        self.age=20
    def set_Sal(self):
        self.sal=500000000.00
e2=Emp()
print(e2.__dict__)
e2.set_Sal()
print(e2.__dict__)

# ---Assign val--- #
class Emp:
    def __init__(self):
        self.name="urmi"
        self.age=20
        self.sal=500000000.00
    def show(self):
        print(self.name,self.age,self.sal,self.dep)
e3=Emp()
print(e3.__dict__)
e3.__dict__['dep']='CSE-AI'
print(e3.__dict__)
e3.show()

# ----delete variable----- #
class Emp:
    def __init__(self):
        self.name="urmi"
        self.age=20
        self.sal=500000000.00
    def show(self):
        print(self.name,self.age,self.sal,self.dep)
e4=Emp()
print(e4.__dict__)
e4.__dict__['dep']='CSE-AI'
print(e4.__dict__)
e4.show()
del e4.__dict__['age']
# e4.show()

# ---- **kwargs-keyword arguments ..collects extra keyword arguments as a dictionary

class Emp:
    def __init__(self,**kwargs):
        self.__dict__.update(kwargs)
    def show(self):
        print(self.name,self.age)

e5=Emp(name="Urmi",age=20)
print(e5.__dict__)
e5.show()
