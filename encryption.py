# ==========================================================
# DecodeLabs Internship Project 2
# Basic Encryption & Decryption (Caesar Cipher)
# ==========================================================

def encrypt(message, shift):
    encrypted = ""

    for char in message:

        # Encrypt uppercase letters
        if 'A' <= char <= 'Z':
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

        # Encrypt lowercase letters
        elif 'a' <= char <= 'z':
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

        # Leave spaces, numbers and symbols unchanged
        else:
            encrypted += char

    return encrypted


def decrypt(message, shift):
    decrypted = ""

    for char in message:

        # Decrypt uppercase letters
        if 'A' <= char <= 'Z':
            decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))

        # Decrypt lowercase letters
        elif 'a' <= char <= 'z':
            decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

        # Leave spaces, numbers and symbols unchanged
        else:
            decrypted += char

    return decrypted


# =========================
# Main Program
# =========================

print("=" * 50)
print("      BASIC ENCRYPTION & DECRYPTION")
print("            Caesar Cipher")
print("=" * 50)

message = input("\nEnter your message: ")
shift = int(input("Enter shift key (1-25): "))

encrypted_message = encrypt(message, shift)
decrypted_message = decrypt(encrypted_message, shift)

print("\n" + "=" * 50)
print("Original Message  :", message)
print("Encrypted Message :", encrypted_message)
print("Decrypted Message :", decrypted_message)
print("=" * 50)
