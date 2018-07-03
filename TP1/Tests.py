import string
global str

def encode_decode(str, decode = False):
    # Create string for lower and upper alphabet and their reverts
    alphabet = string.ascii_uppercase
    lowerAlphabet = string.ascii_lowercase
    al_encode = alphabet[::-1]
    lowerAl_encode = lowerAlphabet[::-1];

    res = ""

    if decode:
        # Needs to Decode the string
        for c in str:
            # Check for lower or upper case
            usingAlphabet = alphabet if c.istitle() else lowerAlphabet
            usingAlphabet_encode = al_encode if c.istitle() else lowerAl_encode

            n = usingAlphabet_encode.find(c)

            # Check for value
            if n < 0:
                res = res + c
            else:
                res = res + usingAlphabet[n]
    else:
        # Needs to Encode the string
        for c in str:
            # Check for lower or upper case
            usingAlphabet = alphabet if c.istitle() else lowerAlphabet
            usingAlphabet_encode = al_encode if c.istitle() else lowerAl_encode

            n = usingAlphabet.find(c)

            # Check for value
            if n < 0:
                res = res + c
            else:
                res = res + usingAlphabet_encode[n]



    print("Message : " + res)

encode_decode("Cette méthode de chiffrement par substitution est trop simple !")
encode_decode("Xvggv négslwv wv xsruuivnvmg kzi hfyhgrgfgrlm vhg gilk hrnkov !", True)

def getMostUsedCharacter(str):
    # Create variables
    characters = []
    mostUsed = ("default", 0)

    # For each character add or update characters
    for c in str:
        characters = addToArray(characters, c)

    # Retrieve the higher value
    for (val, count) in characters:
        if count > mostUsed[1]:
            mostUsed = (val, count)

    return mostUsed

def addToArray(arr, value):
    # Check if we need to add the value
    needsToAdd = True;

    # For each value in the array -> Update the good one
    for i, (val, count) in enumerate(arr):
        if val == value and value != ' ' and value != ',' and value != '.':
            arr[i] = (val, count + 1)
            needsToAdd = False;
            break

    # If array is empty or if the value is not already in the array
    if len(arr) == 0 or needsToAdd:
        arr.append((value, 1))
        return arr


    return arr

def getIndex(c):
    # Define some variables
    c = c.upper();
    letterIndex = 0;

    # For each value in the alphabet -> Get the index of the asked one
    for i in range(0, len(string.ascii_uppercase)):
        if string.ascii_uppercase[i] == c:
            letterIndex = i

    return letterIndex;

def decode(str):
    # Define alphabets
    upperAlphabet = string.ascii_uppercase
    lowerAlphabet = string.ascii_lowercase

    muc = getMostUsedCharacter(str)
    #print(muc)
    distance = getIndex(muc[0]) - 4 # -4 to have the distance between E and the character
    #print(distance)

    res = ""

    for c in str:
        #print(c)
        if c == ' ' or c == '.' or c == ',':
            res = res + c
        else:
            usingAlphabet = upperAlphabet if c.istitle() else lowerAlphabet;
            i = getIndex(c)
            i = (i + distance) % 25 # 25 because array start with 0

            #print(i)

            res = res + usingAlphabet[i]

    print(res)



print()
print(getMostUsedCharacter("Xvggv négslwv wv xsruuivnvmg kzi hfyhgrgfgrlm vhg gilk hrnkov !"))



toEncode = "Wikipédia est un projet d’encyclopédie collective en ligne, universelle, multilingue et fonctionnant sur le principe du wiki. Ce projet vise à offrir un contenu librement réutilisable, objectif et vérifiable, que chacun peut modifier et améliorer. Wikipédia est définie par des principes fondateurs. Son contenu est sous licence Creative Commons BY-SA. Il peut être copié et réutilisé sous la même licence, sous réserve d'en respecter les conditions. Les rédacteurs des articles de Wikipédia sont essentiellement bénévoles. Ils coordonnent leurs efforts au sein d'une communauté collaborative, sans dirigeant."
toDecode = "Drprkéwrz vhg fm kilqvg w’vmxbxolkéwrv xloovxgrev vm ortmv, fmrevihvoov, nfogrormtfv vg ulmxgrlmmzmg hfi ov kirmxrkv wf drpr. Xv kilqvg erhv à luuiri fm xlmgvmf oryivnvmg iéfgrorhzyov, lyqvxgru vg eéirurzyov, jfv xszxfm kvfg nlwrurvi vg znéorlivi. Drprkéwrz vhg wéurmrv kzi wvh kirmxrkvh ulmwzgvfih. Hlm xlmgvmf vhg hlfh orxvmxv Xivzgrev Xlnnlmh YB-HZ. Ro kvfg êgiv xlkré vg iéfgrorhé hlfh oz nênv orxvmxv, hlfh iéhviev w'vm ivhkvxgvi ovh xlmwrgrlmh. Ovh iéwzxgvfih wvh zigrxovh wv Drprkéwrz hlmg vhhvmgrvoovnvmg yéméelovh. Roh xlliwlmmvmg ovfih vuuligh zf hvrm w'fmv xlnnfmzfgé xloozylizgrev, hzmh wrirtvzmg."
# Problème => D -> W = 19 / E -> V = 17

encode_decode(toEncode, False)
print(getMostUsedCharacter(toDecode))
decode(toDecode)