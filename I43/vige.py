# Correction à faire pour prendre en compte les majuscules.


def crypt_vig(message, cle):
    code = ""
    for lettre in "',-;:!?. ":  # Suppression de la ponctuation
        message = message.replace(lettre, "")
    for i, c in enumerate(message):
        d = cle[i % len(cle)]
        d = ord(d) - 97
        code += chr((ord(c)-97+d) % 26+97)
    return code


def decrypt_vig(message, cle):
    code = ""
    for i, c in enumerate(message):
        d = cle[i % len(cle)]
        d = ord(d) - 97
        d = 26 - d
        code += chr((ord(c)-97+d) % 26+97)
    return code


def DecodeVigenere(message, cle):
    return decrypt_vig(message, cle)


def CodeVigenere(message, cle):
    return crypt_vig(message, cle)


message = 'lhobrhqhxhxh'
message2 = 'hakuna matata'
cle = 'eh'

print("Message code     : ", CodeVigenere(message2, cle))
print("                                                   ")
print("Message decode   : ", DecodeVigenere(message, cle))
