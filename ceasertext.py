def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - start + shift) % 26 + start)
        else:
            encrypted_text += char
    
    return encrypted_text

def main():
    while True:
        action = input("Do you want to (e)ncrypt or (d)ecrypt a message? (q to quit): ").lower()
        if action == 'q':
            print("Goodbye!")
            break

        if action not in ['e', 'd']:
            print("Invalid option. Please enter 'e' to encrypt or 'd' to decrypt.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter shift value (0-25): "))

        # Perform encryption and decryption
        if action == 'e':
            encrypted_message = caesar_cipher(message, shift)
            decrypted_message = caesar_cipher(encrypted_message, -shift)
        else:
            decrypted_message = caesar_cipher(message, -shift)
            encrypted_message = caesar_cipher(decrypted_message, shift)

        print(f"Encrypted message: {encrypted_message}")
        print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
