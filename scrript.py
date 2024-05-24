# Ask user if they want to generate a password or not.
# if they do, ask for password length
# Generate a password
# Display the password
# if they said no initially, exit the programme

import random
import string

def main():
    password_length = int(input("How long do you want your password to be? ")) # Ask user for password length
    password = generate_password(password_length) # Generate password   
    print(password) # Display password
    return

def generate_password(password_length): 
    
    password = ""
    for i in range(password_length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password 
main()