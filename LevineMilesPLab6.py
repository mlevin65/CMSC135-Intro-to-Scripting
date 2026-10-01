

def caesar_cipher(text, key):
    """Encrypts the given text using Caesar Cipher and returns the encrypted text"""
    result = ""

    # Iterate through each character in the input text
    for char in text:
        if char.isalpha():
            # Convert the character to its ASCII code
            ascii_code = ord(char)

            # Determine if the character is uppercase or lowercase
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            # Apply the key to the character's ASCII code, wrapping around if necessary
            shifted_ascii = (ascii_code - base + key) % 26 + base

            # Convert the shifted ASCII code back to a character and add it to the result
            result += chr(shifted_ascii)
        else:
            # Add non-alphabetic characters to the result as-is
            result += char

    return result


encrypted_text = caesar_cipher("caesar", 2)
print(encrypted_text)
