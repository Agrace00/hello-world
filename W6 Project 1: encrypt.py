"""
File: encrypt.py
Encypts an input string of lowercase letters and prints
the result.  The other input is the distance value.
"""
def encrypt(plaintext, distance):
  ciphertext = ""
  for char in plaintext:
    if char.isalpha():

      if char.isupper():
        new_char = chr((ord(char) - ord('A') + distance) % 26 + ord('A'))

      else:
        new_char = chr((ord(char) - ord('a') + distance) % 26 + ord('a'))
 
    else:
      new_char = char
    ciphertext += new_char
  return ciphertext

plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))

ciphertext = encrypt(plainText, distance)
print("Encrypted text:", ciphertext)
