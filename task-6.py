"""6.	Write a Python function that divides two numbers and handles the case where the divisor is zero by returning a custom error message.
   """     
def divide_numbers(num1, num2):
    try:
        # Attempt to divide num1 by num2
        result = num1 / num2
        return result
    except ZeroDivisionError:
        # Return a custom error message if division by zero is attempted
        return "Error: Division by zero is not allowed."

# Example usage
numerator = 10
denominator = 0

result = divide_numbers(numerator, denominator)
print(result)  # Output: Error: Division by zero is not allowed.

denominator = 2
result = divide_numbers(numerator, denominator)
print(result)  # Output: 5.0
