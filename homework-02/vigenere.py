def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    keyword_upper = keyword.upper()
    key_len = len(keyword_upper)
    
    for i, char in enumerate(plaintext):
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            # Получаем сдвиг из ключа
            shift = ord(keyword_upper[i % key_len]) - ord('A')
            
            # Шифруем букву
            original_pos = ord(char) - base
            encrypted_pos = (original_pos + shift) % 26
            ciphertext += chr(base + encrypted_pos)
        else:
            ciphertext += char
    
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    keyword_upper = keyword.upper()
    key_len = len(keyword_upper)
    
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            
            shift = ord(keyword_upper[i % key_len]) - ord('A')
            
            encrypted_pos = ord(char) - base
            original_pos = (encrypted_pos - shift) % 26
            plaintext += chr(base + original_pos)
        else:
            plaintext += char
    
    return plaintext