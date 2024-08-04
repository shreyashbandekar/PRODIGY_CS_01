def encrypt(text, shift):
    """Encrypts the given text using Caesar Cipher with the specified shift."""
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shift and ensure it wraps around the alphabet
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    
    return result

def decrypt(text, shift):
    """Decrypts the given text using Caesar Cipher with the specified shift."""
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Encryption/Decryption")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    
    if choice not in ('E', 'D'):
        print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (integer): "))

    if choice == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    else:
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
