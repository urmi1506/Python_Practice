
'''
Build an Employee Management System:

Requirements:
1. Base class: Employee
   - name, employee_id, salary
   - get_details() method
   - give_raise(percent) method

2. Child class: Manager(Employee)
   - department attribute
   - team_size attribute  
   - Override get_details() to include dept
   - add bonus() method (10% extra)

3. Child class: Developer(Employee)
   - programming_language attribute
   - Override get_details() to include language
   - add overtime() method (salary + 20%)

4. Decorator: @log_action
   - Prints "Action: <function_name> called"
   - Apply it to give_raise() and bonus()

Expected Output:
─────────────────────────────────────────
  Employee : Alice | ID: E001 | Salary: ₹50000
  Manager  : Bob   | ID: M001 | Dept: Engineering
  Developer: Charlie | ID: D001 | Language: Python
─────────────────────────────────────────
Action: give_raise called
   Alice's new salary: ₹55000
─────────────────────────────────────────
Action: bonus called
   Bob's bonus salary: ₹60500
'''



def log_action(func):
    """Your decorator here."""
    def wrapper(*args, **kwargs):
        print(f"Action: {func.__name__} called")
        return func(*args,**kwargs)
    return wrapper


class Employee:
    def __init__(self, name, emp_id, salary):
        self.name =name 
        self.emp_id =emp_id
        self.salary =salary

    def get_details(self):
        # Print employee details
        print(f"Employee : {self.name} | ID: {self.emp_id} | Salary: ₹{self.salary}")


    @log_action
    def give_raise(self, percent):
        # Calculate and apply raise
        self.salary += self.salary * (percent / 100.0)
        print(f"{self.name}'s new salary: ₹{int(self.salary)}")


class Manager(Employee):
    def __init__(self, name, emp_id, salary, department, team_size):
        # Call parent __init__ using super()
        super().__init__(name ,emp_id,salary)
        # Add manager specific attributes
        self.department =department
        self.team_size =team_size

    def get_details(self):
        # Override parent method
        print(f"Manager  : {self.name} | ID: {self.emp_id} | Dept: {self.department}")

    @log_action
    def bonus(self):
        # Add 10% bonus
        bonus_salary = self.salary + (self.salary * 0.10)
        print(f"{self.name}'s bonus salary: ₹{int(bonus_salary)}")
        


class Developer(Employee):
    def __init__(self, name, emp_id, salary, language):
        # Your code here
        super().__init__(name ,emp_id,salary)
        self.language = language
        

    def get_details(self):
        print(f"Developer: {self.name} | ID: {self.emp_id} | Language: {self.language}")


    def overtime(self):
        # Add 20% overtime
        overtime_salary = self.salary + (self.salary * 0.20)
        print(f"{self.name}'s overtime salary: ₹{int(overtime_salary)}")


# Test Cases:
emp = Employee("Alice",   "E001", 50000)
mgr = Manager("Bob",     "M001", 55000, "Engineering", 10)
dev = Developer("Charlie","D001", 60000, "Python")

emp.get_details()
mgr.get_details()
dev.get_details()

print("─────────────────────────────────────────")
emp.give_raise(10)

print("─────────────────────────────────────────")
mgr.bonus()

print("─────────────────────────────────────────")
dev.overtime()
