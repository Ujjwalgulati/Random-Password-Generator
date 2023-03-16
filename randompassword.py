import random
import string

def generate_password(length):
    # Define the character sets for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all the character sets
    all_chars = lowercase + uppercase + digits + symbols

    # Generate the password
    password = ''.join(random.choice(all_chars) for i in range(length))

    return password

# Test the function
print(generate_password(8)) # Generate an 8-character password