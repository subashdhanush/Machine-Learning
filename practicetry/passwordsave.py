import random
import string

print("🔐 Custom Password Generator")

# Ask user for options
length = int(input("Enter desired password length: "))
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

# Build the character set
characters = ""
if use_upper:
    characters += string.ascii_uppercase
if use_lower:
    characters += string.ascii_lowercase
if use_digits:
    characters += string.digits
if use_symbols:
    characters += string.punctuation

if not characters:
    print("Error: No character sets selected!")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"\nGenerated Password: {password}")

    # Optional: Save to file
    save = input("Save this password to 'passwords.txt'? (y/n): ").lower()
    if save == 'y':
        with open("passwords.txt", "a") as f:
            f.write(password + "\n")
        print("Password saved to passwords.txt ✅")
