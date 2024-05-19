def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            if char.isupper():
                # Shift uppercase letters
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                # Shift lowercase letters
                result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If the character is not a letter, keep it unchanged
            result += char
    return result

def main():
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper()
    if choice == 'E':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted_message = caesar_cipher(message, shift)
        print("Encrypted message:", encrypted_message)
    elif choice == 'D':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))
        decrypted_message = caesar_cipher(message, -shift)  # Decrypting by shifting in the opposite direction
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
