import string, sys, getopt

BLOCK_SIZE = 64
INITIALIZER_VECTOR = bytes(b'\xaa\xe5\xcc:\xa3(\xb9\x10\x9b-\x196\xeb\xa7|\xa3\xa8W\xf9\x17\xb55\xc2\xff\xb0\x08Q9`\xac:\xbfi\xb3\xbe\xc5~\xa1/\xc8\xc18\x93f+\rq\xd8\xeb\xe3H\xe6\x8e\x037\x87+\xb7\xefY\x8bp\xd6\x11')
PASS_PHRASE = bytes(b'0010000100000010000010001000001000010011100111100000111110011001')

def cbc_xor(first_block,second_block):
    """
        XOR logique pour CBC

        Paramètres:
        -----
        first_block : [bytes]
            first block argument soumis pour le XOR logique
        second_block : [bytes]
            second block argument soumis pour le XOR logique

        Retourne:
        ------
        List(bytes)
            Résultat du XOR logique

    """
    return [a^b for (a,b) in zip(first_block,second_block) ]


def cbc_create_blocks(data,padding = False):
    blocks = list()
    for i in range(0,len(data),BLOCK_SIZE):
        blocks.append(data[i:i+BLOCK_SIZE])
        if padding:
            if (i+BLOCK_SIZE) > len(data):
                needed_size = (i+BLOCK_SIZE)-len(data)
                last_block = data[i:i+BLOCK_SIZE]
                for y in range(0,needed_size):
                    last_block += b'0'
                blocks.append(last_block)
    return blocks


def cbc_encrypt(data,filename):
    """
        Méthode de chiffrement CBC
        Chiffre les données avec la méthode CBC et les sauvegarde dans un fichier donné par l'utilisateur

        Paramètres:
        -----
        data : bytes
            Les données
        filename : string
            Le nom du fichier

    """
    blocks = cbc_create_blocks(data,True)
    iv = INITIALIZER_VECTOR
    encrypted_blocks = list()
    for block in blocks:
        #XOR Block
        cyphered_block = cbc_xor(block,iv)
        # Encrypt block
        cyphered_block = cbc_xor(cyphered_block,PASS_PHRASE)
        iv = cyphered_block
        encrypted_blocks.append(cyphered_block)

    cbc_write_bytes_file(encrypted_blocks,filename)


def cbc_decrypt(filename):
    """
        Méthode de déchiffrement CBC
        Charge un fichier précédemment chiffré avec l'algorithme CBC
        Déchiffre le fichier et le ré-écrit

        Paramètres:
        -----
        filename : string
            Fichier a déchiffrer

    """
    datas = cbc_read_bytes_file(filename)
    blocks_data = cbc_create_blocks(datas)

    decrypted_data = list()
    iv = INITIALIZER_VECTOR
    for cyphered_block in blocks_data:
        #DECRYPT BLOCK
        uncyphered_block = cbc_xor(PASS_PHRASE,cyphered_block)
        # XOR BLOCK
        uncyphered_block = cbc_xor(iv,uncyphered_block)
        decrypted_data.append(uncyphered_block)
        iv = cyphered_block

    cbc_write_bytes_file(decrypted_data,filename)


def cbc_read_bytes_file(filename):
    """
        Méthode de lecture d'un fichier

        Paramètres:
        -----
        filename : string
            Fichier à lire

        Retourn:
        ------
        bytes
            Données depuis le fichier

    """
    with open(filename,'rb') as f:
        data = bytes(f.read())
        return data


def cbc_write_bytes_file(datas,filename):
    """
        Méthode d'écriture d'un fichier

        Paramètres:
        -----
        datas : List(bytes)
            Les données à écrire dans le fichier
        filename : string
            Fichier
    """
    with open(filename,"wb") as f:
        for data in datas:
            f.write(bytearray(data))


