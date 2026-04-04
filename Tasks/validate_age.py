def validate_age(func):
    """Validate age before running function."""
    def wrapper(*args,**kwargs):
        # Get age from args
        age = args[1]

        # Validation
        if age < 0 or age > 120:
            print(f"Invalid age: {age}. Profile not created.")
            return  

        # If valid, call original function
        return func(*args, **kwargs)
    return wrapper

@validate_age
def create_profile(name, age):
    print(f"Profile created: {name}, Age: {age}")

create_profile("Alice", 25)     
create_profile("Bob", -5)      
create_profile("Charlie", 150)  
create_profile("Diana", 0)     