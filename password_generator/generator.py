import random
import string

def generate_password(length=8, complexity=1):
    """
    Generates a random password of a specified length and complexity.
    """
    # Define the character sets to use for different complexity levels
    if complexity == 1:
        charset = string.ascii_letters
    elif complexity == 2:
        charset = string.ascii_letters + string.digits
    elif complexity == 3:
        charset = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random characters from the chosen character set
    password = ''.join(random.choice(charset) for _ in range(length))
    return password



