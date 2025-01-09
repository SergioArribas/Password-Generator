import random
import string

def generate_password(length=12):
    character = string.ascii_letters + string.digits + string.punctuation
    password = "".join (random.choices(character, k=length))
    return password

if __name__ == "__main__":
    print("===Pasword Generator===")
    try:
        length = int(input("How many characters should the password have? (minimum 8): "))
        if length < 8:
            print("The password must be at least 8 charactes long. ")
        else:
            password = generate_password(length)
            print(f"Your generated password is: {password}" )
    except ValueError:
        print("Please enter a valid number")