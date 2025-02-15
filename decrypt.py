"""
File: decrypt.py
Decypts an input string of lowercase letters and prints
the result.  The other input is the distance value.
"""

def decrypt_caesar(ciphertext, distance):
    plaintext = ''
    for char in ciphertext:
        if char.isprintable():  
            if char.isalpha():
                
                if char.isupper():
                    plaintext += chr((ord(char) - distance - 65) % 26 + 65)
                else:
                    plaintext += chr((ord(char) - distance - 97) % 26 + 97)
            else:
               
                plaintext += chr((ord(char) - distance) % 256)
        else:
            
            plaintext += char
    return plaintext

def main():
    encrypted_text = input("Enter the encrypted text: ")
    distance = int(input("Enter the distance value: "))
    
    decrypted_text = decrypt_caesar(encrypted_text, distance)
    
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
