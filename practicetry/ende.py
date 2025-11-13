def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            print("shifted",shifted)
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("\n--- Simple Encryption & Decryption ---")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt? ").lower()

    if choice == 'e':
        text = input("Enter the text to encrypt: ")
        shift = int(input("Enter the shift value (1-25): "))
        encrypted_text = encrypt(text, shift)
        print(f"Encrypted Text: {encrypted_text}")
    elif choice == 'd':
        text = input("Enter the text to decrypt: ")
        shift = int(input("Enter the shift value (1-25): "))
        decrypted_text = decrypt(text, shift)
        print(f"Decrypted Text: {decrypted_text}")
    else:
        print("Invalid choice. Please select (E) to encrypt or (D) to decrypt.")

if __name__ == "__main__":
    main()
