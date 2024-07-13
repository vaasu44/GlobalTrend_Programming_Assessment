"""
5.	Write a Python decorator that measures the execution time of a function and logs it. Apply this decorator to a function that performs a computationally expensive task.
"""
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
# Decorator that measures the execution time of a function and logs it.
def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record the end time
        execution_time = end_time - start_time  # Calculate the execution time
        logging.info(f"Executed {func.__name__} in {execution_time:.4f} seconds")  # Log the execution time
        return result
    return wrapper

@time_logger
def computationally_expensive_task(n):
    """
    Function that performs a computationally expensive task.
    For demonstration purposes, it calculates the sum of squares of numbers from 1 to n."""
    
    result = sum(i ** 2 for i in range(1, n + 1))
    return result

# Example usage
n = 1000000
result = computationally_expensive_task(n)
print(f"The sum of squares from 1 to {n} is : {result}")
