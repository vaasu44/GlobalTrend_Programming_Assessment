"""
4.	Write a Python function that takes two numbers and an operator (as a string) and performs the corresponding arithmetic operation (addition, subtraction, multiplication, or division).
"""
def calculate(num1, num2, operator):
    
    # Perform the arithmetic operation based on the operator
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check if the second number is zero to avoid division by zero
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2
    else:
        # Raise an error if the operator is not valid
        raise ValueError("Invalid operator. Please use one of '+', '-', '*', '/'.")

# Example usage
num1 = 10
num2 = 5
operator1 = '+'
num3 = 10
num4 = 5
operator2 = '-'

result = calculate(num1, num2, operator1)
print(f"The result of {num1} {operator1} {num2} is {result}")

result = calculate(num1, num2, operator2)
print(f"The result of {num3} {operator2} {num4} is {result}")
