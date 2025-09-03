class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."
    
    def sleep(self):
        return f"{self.name} is sleeping."
    
class Dog(Animal):
    def bark(self):
        return f"{self.name} says Woof!"    
    
class Cat(Animal):
    def meow(self):
        return f"{self.name} says Meow!"
    
dog = Dog("Buddy")      
cat = Cat("Whiskers")
print(dog.eat())
print(dog.bark())
print(cat.sleep())
print(cat.meow())
    

    