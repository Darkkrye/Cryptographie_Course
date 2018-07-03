import string
global str

# Chiffre le message en se basant sur l'algorithme de César
def encode(str, key):
    encodedStr = ""

    # Boucle sur les caractères
    for i in range(len(str)):
        c = str[i]

        # Vérification de la casse
        if c in string.ascii_uppercase:
            encodedStr += chr((ord(c) + key - ord('A')) % 26 + ord('A'))
        elif c in string.ascii_lowercase:
            encodedStr += chr((ord(c) + key - ord('a')) % 26 + ord('a'))
        else:
            encodedStr += c

    return encodedStr


# Decode le message en se basant sur l'algorithme de César
def decodeWithKey(encodedStr, key):
    decodedStr = ""

    for i in range(len(encodedStr)):
        character = encodedStr[i]

        # Vérification de la casse
        if character in string.ascii_uppercase:
            decodedStr += chr((ord(character) + (- key) - ord('A')) % 26 + ord('A'))
        elif character in string.ascii_lowercase:
            decodedStr += chr((ord(character) + (- key) - ord('a')) % 26 + ord('a'))
        else:
            decodedStr += character

    return decodedStr


def frequency(data):
    freq = [0]*26

    for character in data.upper():
        if character in string.ascii_uppercase:
            freq[ord(character) - ord('A')] += 1

    return freq


def decodeWithoutKey(encodedStr):
    frequencies = frequency(encodedStr) # Récupération de la fréquence d'apparition de chaque lettre dans la chaîne
    max_value = max(frequencies)
    key = frequencies.index(max_value) - 4 # -4 à cause de l'emplacement de E dans l'alphabet

    return decodeWithKey(encodedStr, key)


print("Original Message => " + toEncode)
toDecode = encode(toEncode, 6)
print("Encoded String => " + toDecode)
decodedWithKey = decodeWithKey(toDecode, 6)
print("Decoded String with Key => " + decodedWithKey)
decodedWithoutKey = decodeWithoutKey(toDecode)
print("Decoded String without Key => " + decodedWithoutKey)