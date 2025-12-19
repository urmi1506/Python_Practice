class User:
    def __init__(self ,name ,email , role):
        self.name = name
        self.email = email
        self.role = role



    def display_user(self):
        return f"Name: {self.name}, Email: {self.email}, Role: {self.role}"
    
    def update_name(self, new_name):
        self.name = new_name

    def update_role(self, new_role):
        if new_role not in ["admin","staff","viewer"]:
            raise ValueError("Attempting invalid role...\nInvalid role. Allowed roles: admin, staff, viewer")
        self.role = new_role

    def update_email(self, new_email):
        raise Exception("Email update not allowed.")
        

obj1 = User("Urmi", "ab@example.com", "admin")
obj2 = User ("Rutvik" , "abc@example.com", "viewer")
obj3 = User("Aachal","xyz@example.com", "staff")

print(obj1.display_user())

obj1.update_role("staff")
print(obj1.display_user())

try:
    obj3.update_email("def@example.com")
except Exception as e:
    print(e)

try:
   obj2.update_role("user")
except ValueError as ve:
    print(ve)
