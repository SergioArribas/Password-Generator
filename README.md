# Password Generator

This is a Python script that generates a random password. The script allows the user to specify the desired length of the password, and it includes uppercase and lowercase letters, numbers, and special characters by default.

## What the Code Does
1. The script defines a function `generate_password(length=12)` that generates a random password of the specified length. 
2. It uses the `string` module to access characters such as:
   - Uppercase and lowercase letters (`string.ascii_letters`)
   - Digits (`string.digits`)
   - Special characters (`string.punctuation`)
3. The script prompts the user to enter the desired password length (minimum 8 characters).
4. The `generate_password` function randomly selects characters from the available set and combines them to form a password.
5. The generated password is then displayed to the user.

## How to Use
1. Run the Python script.
2. Enter the desired password length when prompted.
3. The script will output a randomly generated password.