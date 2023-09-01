# Dictionary mapping for switch/case logic
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

# Create a dictionary to map operation names to functions
operation_dict = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide
}

# User input
operation_name = input("Enter operation name (add, subtract, multiply, divide): ")

# Check if the operation is in the dictionary
if operation_name in operation_dict:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    
    # Call the corresponding function from the dictionary
    result = operation_dict[operation_name](x, y)
    print("Result:", result)
else:
    print("Invalid operation name")
