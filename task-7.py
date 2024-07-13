"""7.	Write a Python function to compute the nth Fibonacci number using recursion."""
def fibonacci(n):
    # Base case: the first and second Fibonacci numbers are both 1
    if n <= 0:
        raise ValueError("Input should be a positive integer.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage
n = 10
result = fibonacci(n)
print(f"The {n}th Fibonacci number is {result}")
