import typing as tp

en_abc = 'abcdefghijklmnopqrstuvwxyz'
en_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ru_ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet = en_abc + en_ABC + ru_abc + ru_ABC
def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

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
    #en_a = str.maketrans(en_abc[ : -shift], en_abc[shift - 1 : ])
    #en_A = str.maketrans(en_ABC[ : -shift], en_ABC[shift - 1 : ])
    #ru_a = str.maketrans(ru_abc[ : -shift], ru_abc[shift - 1 : ])
    #ru_A = str.maketrans(ru_ABC[ : -shift], ru_ABC[shift - 1 : ])

    #trans = str.maketrans ({en_abc[i]:en_abc[i+shift],    en_ABC[i]:en_ABC[i+shift],   ru_abc[i]:ru_abc[i+shift],   ru_ABC[i]:ru_ABC[i+shift]}, for i in range(45))
    tempEn1 = en_abc[shift:] + en_abc[:shift]
    tempEn2 = en_ABC[shift:] + en_ABC[:shift]
    tempRu1 = ru_abc[shift:] + ru_abc[:shift]
    tempRu2 = ru_ABC[shift:] + ru_ABC[:shift]
    tempAlpha = tempEn1 + tempEn2 + tempRu1 + tempRu2
    #print(tempAlpha)
    #print(alphabet)
    trans = str.maketrans(alphabet, tempAlpha)

    ciphertext = plaintext.translate(trans)

    return ciphertext

#word = 'PYTHON'
#print(encrypt_caesar(word))


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
    tempEn1 = en_abc[shift:] + en_abc[:shift]
    tempEn2 = en_ABC[shift:] + en_ABC[:shift]
    tempRu1 = ru_abc[shift:] + ru_abc[:shift]
    tempRu2 = ru_ABC[shift:] + ru_ABC[:shift]
    tempAlpha = tempEn1 + tempEn2 + tempRu1 + tempRu2

    trans = str.maketrans(tempAlpha, alphabet)

    plaintext = ciphertext.translate(trans)
    # PUT YOUR CODE HERE
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
