## Python Control Flow and Exception Handling

This README provides examples and explanations of how to use control flow structures like if/else statements, try/except statements, and dictionary mapping for switch/case logic in Python.

## 1. Conditional Execution with if/else Statements

```python
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
2. Exception Handling with try/except Statements
python
Copy code
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print("An unexpected error occurred:", e)
3. Using Dictionary Mapping for Switch/Case Logic
Python does not have a built-in switch/case statement, but you can use dictionaries to simulate it. Here's an example:

python
Copy code
def add(x, y):
    return x + y

# Define other operation functions (subtract, multiply, divide)

# Create a dictionary to map operation names to functions
operation_dict = {
    'add': add,
    # Add other operations and their corresponding functions here
}

# User input and execution
operation_name = input("Enter operation name (add, subtract, multiply, divide): ")

if operation_name in operation_dict:
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    # Call the corresponding function from the dictionary
    result = operation_dict[operation_name](x, y)
    print("Result:", result)
else:
    print("Invalid operation name")
Feel free to adapt and use these examples in your Python projects as needed. They cover the basics of control flow and exception handling in Python.
---

## Resources

- [Python ternary operators](https://book.pythontips.com/en/latest/ternary_operators.html)
- [PEP 8 - Style Guide for Python Code][pep 8]

[pep 8]: https://peps.python.org/pep-0008/
```
