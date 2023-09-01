# Handling exceptions with try/except statements
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
