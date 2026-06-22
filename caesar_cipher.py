def encrypt(text, shift):
    """
    Encrypts the given text using Caesar Cipher.
    """
    result = ""
    for char in text:
        # Handle uppercase letters
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        
        # Handle lowercase letters
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        
        # Leave non-alphabet characters unchanged (spaces, punctuation, numbers)
        else:
            result += char
    return result


def decrypt(text, shift):
    """
    Decrypts the given text using Caesar Cipher.
    """
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            result += char
    return result


def main():
    print("=" * 60)
    print(" CAESAR CIPHER - BASIC ENCRYPTION & DECRYPTION")
    print("Cyber Security Project 2")
    print("=" * 60)
    
    while True:
        print("\n--- MENU ---")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Encrypt and then Decrypt (Test)")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '4':
            print("\nThank you for completing Project 2! Stay secure! 🔒")
            break
            
        if choice not in ['1', '2', '3']:
            print(" Invalid choice! Please try again.")
            continue
        
        # Get input text
        text = input("\nEnter your message: ")
        
        # Get shift key with validation
        while True:
            try:
                shift = int(input("Enter shift key (1-25): "))
                if 1 <= shift <= 25:
                    break
                else:
                    print(" Shift must be between 1 and 25.")
            except ValueError:
                print(" Please enter a valid number.")
        
        if choice == '1':
            encrypted = encrypt(text, shift)
            print("\n" + "-"*50)
            print(f"Original  : {text}")
            print(f"Encrypted : {encrypted}")
            print("-"*50)
            
        elif choice == '2':
            decrypted = decrypt(text, shift)
            print("\n" + "-"*50)
            print(f"Encrypted : {text}")
            print(f"Decrypted : {decrypted}")
            print("-"*50)
            
        elif choice == '3':
            encrypted = encrypt(text, shift)
            decrypted = decrypt(encrypted, shift)
            print("\n" + "-"*50)
            print(f"Original   : {text}")
            print(f"Encrypted  : {encrypted}")
            print(f"Decrypted  : {decrypted}")
            print("-"*50)
            
            # Verification
            if decrypted == text:
                print(" Success! Encryption and Decryption working perfectly.")
            else:
                print(" Something went wrong.")


if __name__ == "__main__":
    main()