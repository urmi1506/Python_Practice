def calculate(operation, *numbers):
    # Print operation and numbers
    print(f"Operation: {operation} | Numbers: {numbers}", end="")
    
    # Handle different operations
    if operation == "add":
        result = sum(numbers)
        print(f" | Result: {result}")
    elif operation == "multiply":
        result = 1
        for num in numbers:
            result *= num
        print(f" | Result: {result}")
    else:
        print(f" | Result: Operation '{operation}' not supported")

calculate("add", 1, 2, 3, 4)        
calculate("multiply", 2, 3, 4)    
calculate("add", 10, 20)           
calculate("divide", 10, 2)           