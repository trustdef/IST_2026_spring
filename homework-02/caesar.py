import typing as tp

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    Based on implementation from dev.to

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            shifted = (ord(char) - start + shift) % 26
            ciphertext += chr(start + shifted)
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            shifted = (ord(char) - start - shift) % 26
            plaintext += chr(start + shifted)
        else:
            plaintext += char
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    Returns the shift that produces the most words from the dictionary.
    """
    best_shift = 0
    best_count = 0

    for shift in range(26):
        decrypted = decrypt_caesar(ciphertext, shift)

        # Разбиваем на слова
        words = []
        current_word = ""
        for ch in decrypted:
            if ch.isalpha():
                current_word += ch.upper()
            else:
                if current_word:
                    words.append(current_word)
                    current_word = ""
        if current_word:
            words.append(current_word)

        count = sum(1 for word in words if word in dictionary)

        if count > best_count:
            best_count = count
            best_shift = shift

    return best_shift