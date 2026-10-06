import random
import string

Password_Length= int(input("Enter password length :")) 
def generate_password(Password_Length):
    character = string.ascii_letters + string.digits+"!@#$%^&*"
    password = ''.join(random.choice(character) for i in range(Password_Length))
    return password

if Password_Length >= 8:
    print("Valid password length")
    print(generate_password(Password_Length))
else:
    print("Invalid password length. Minimum is 8.")
