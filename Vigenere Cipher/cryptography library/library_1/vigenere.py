def encrypt_vigenere(plaintext, key):
    encrypted_data = []
    key = key.upper()
    key_index = 0

    for c in plaintext:
        if c.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if c.isupper():
                encrypted_data.append(chr(ord(c) - ord('A') + shift))
            else:
                encrypted_data.append(chr(ord(c) - ord('a') + shift))
            key_index = (key_index + 1) % len(key) 
        else:
            encrypted_data.append(c)

    return "".join(encrypted_data)

def decrypt_vigenere(ciphertext, key):
    decrypted_data = []
    key = key.upper()
    key_index = 0

    for c in ciphertext:
        if c.isalpha():
            shift = ord(key[key_index]) - ord('A')
            if c.isupper():
                decrypted_data.append(chr(ord(c) - ord('A') - shift))
            else:
                decrypted_data.append(chr(ord(c) - ord('a') - shift))
        else:
            decrypted_data.append(c)
    
    return "".join(decrypted_data)


def break_vigenere(ciphertext):
    #Will be write 
