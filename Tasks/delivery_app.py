# Step 1: Base class first
class User:
    def __init__(self, name, email, password):
        self.name=name
        self.email=email
        self.password=password
        
    def login(self):
        # print login message
        print(f"{self.name} logged in successfully .")
        
    def logout(self):
        # print logout message
        print(f"{self.name} logged out.")


# Step 2: Customer child
class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)   
        
    def place_order(self, item):
        # print order message
        print(f"{self.name} placed order for {item}")


# Step 3: DeliveryPartner child  
class DeliveryPartner(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)   

    def accept_delivery(self,order_id):
        print(f"{self.name} accepted delivery for order {order_id}")


# Step 4: RestaurantOwner child
class RestaurantOwner(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)   

    def add_menu_item(self,item):
        print(f"{self.name} added {item} to menu")



# Step 5: Test it!
c = Customer("Alice", "alice@gmail.com", "pass123")
d = DeliveryPartner("Raju", "raju@gmail.com", "pass456")
r = RestaurantOwner("Hotel Pune", "hotel@gmail.com", "pass789")

c.login()
c.place_order("Biryani")
c.logout()

d.login()
d.accept_delivery(101)

r.login()
r.add_menu_item("Paneer Butter Masala")