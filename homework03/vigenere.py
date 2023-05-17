en_abc = 'abcdefghijklmnopqrstuvwxyz'
en_ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
ru_ABC = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet = en_abc + en_ABC + ru_abc + ru_ABC

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
    temp = []
    key = keyword * (len(plaintext) - len(keyword) + 1)
    for index, item in enumerate(plaintext):
        if not item.isalpha() or item.isnumeric():
            temp.append(item)
            continue
        islower = item.islower()
        tempItem = item.upper()
        posPlain = en_ABC.find(tempItem)
        posKeyWord = en_ABC.find(key[index].upper())
        shift = posKeyWord
        tempShift = en_ABC[shift:] + en_ABC[:shift]

        res = tempShift[posPlain]
        if islower:
            res = res.lower()

        temp.append(res)


    # PUT YOUR CODE HERE
    return ''.join(temp)

print(encrypt_vigenere("python", "a"))
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
    temp = []
    key = keyword * (len(ciphertext) - len(keyword) + 1)
    for index, item in enumerate(ciphertext):
        if not item.isalpha() or item.isnumeric():
            temp.append(item)
            continue
        islower = item.islower()
        tempItem = item.upper()
        posPlain = en_ABC.find(tempItem)
        posKeyWord = en_ABC.find(key[index].upper())
        shift = -posKeyWord
        tempShift = en_ABC[shift:] + en_ABC[:shift]

        res = tempShift[posPlain]
        if islower:
            res = res.lower()

        temp.append(res)


    # PUT YOUR CODE HERE
    return ''.join(temp)

