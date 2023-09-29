alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def encrypt(plain_text, shift_amount):
    encrypted_text = ""

    for char in plain_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position + shift_amount) % len(alphabet)
            encrypted_text += alphabet[new_position]
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""

    for char in encrypted_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position - shift_amount) % len(alphabet)
            decrypted_text += alphabet[new_position]
        else:
            decrypted_text += char

    return decrypted_text


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == "encode":
    result = encrypt(text, shift)
    print(f"Encoded message: {result}")
elif direction == "decode":
    result = decrypt(text, shift)
    print(f"Decoded message: {result}")
else:
    print("Invalid input. Please enter 'encode' or 'decode'.")
