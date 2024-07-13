"""3.	Write a Python function that generates a random password. The password should contain a mix of uppercase letters, lowercase letters, digits, and special characters.
"""
import random
import string

def generate_password(length=12):
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    
    # Ensure the password contains at least one character from each set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    # Fill the rest of the password length with random characters from all sets
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the resulting list to avoid predictable sequences
    random.shuffle(password)
    
    # Convert the list to a string and return it
    return ''.join(password)

# Example usage
password = generate_password(12)
print("Generated Password is  :", password)
