import random
import string
def generate_password(length=12, use_upper=True, use_lower=True, use_numbers=True, use_special=True):
    '''Generates a strong password based on user-specified criteria.'''
    char_pool=""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase    
    if use_numbers:
        char_pool += string.digits
    if use_special:
        char_pool += "!@#$%^&*()-_=+<>?/"

    if not char_pool:
        return "Error: No character set selected!"

    return "".join(random.choice(char_pool)for _ in range(length))

#interactive user input
print("Welcome to the secure password generator !")
length = int(input(" Enter password length (minimum 8): "))    
if length < 8:
    length = 8 #enforce minimum security

use_upper = input(" Include uppercase letters? (y/n): ").strip().lower() == 'y'
use_lower = input(" Include lowercase letters? (y/n): ").strip().lower() == 'y'
use_numbers = input(" Include numbers? (y/n): ").strip().lower() == 'y'
use_special = input(" Include special characters (y/n): ").strip().lower() == 'y'

password = generate_password(length, use_upper, use_lower, use_numbers, use_special)
print(f"Your generated password: {password}")
