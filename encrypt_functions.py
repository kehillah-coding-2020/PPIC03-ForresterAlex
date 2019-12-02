#common functions for Encryption and Decryption
alpha = "abcdefghijklmnopqrstuvwxyz "
key1 = "ouwckbjmpzyexavrltsfgdqihn "
def scramble2Decrypt(cipherText):
    '''
    takes cipherText as input, and returns plain text, basic 2 rail transposition cipher
    '''
    halfLength = len(cipherText)//2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) <len(evenChars):
        plainText = plainText + evenChars[-1]

    return(plainText)

def scramble2Encrypt(plainText):
    '''
    book issued 2 rail transposition cipher
    '''
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 ++ 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = evenChars + oddChars
    return(cipherText)

def non_binary_trans_cipher_encrypt(string):
    '''
    define 3 rail transposition cipher encryption, takes string as input, returns encrypted text
    '''
    string_len = len(string)
    third_len = len(string)//3
    section_one = ''
    section_two = ''
    section_three = ''
    output = ''
    for i in range(third_len):
        temp = i * 3
        section_three = string[temp-2]
        section_two = string[temp-1]
        section_one = string[temp]
        output = output + section_one + section_two + section_three
    return(output)

def non_binary_trans_cipher_decrypt(string):
    '''
    define 3 rail transposition cipher decryption, takes input of string, returns decrypted text
    '''
    string_len = len(string)
    third_len = len(string)//3
    output = ''
    for i in range(third_len):
        temp = i * 3
        output = output + string[temp] + string[temp-1] + string[temp-2]
    return(output)

def substitutionEncrypt(plainText, key):
    '''
    define substitution encryption function, take input of plain text, and a key, uses "alpha" variable for alphabet defined at the top of the file
    '''
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alpha.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText


def substitutionDecrypt(string, key):
    '''
    #define substitution decryption function, take input of encrypted text, and a key, uses "alpha" variable for alphabet
    '''
    string = string.lower()
    plainText = ""
    for ch in string:
        idx = key.find(ch)
        plainText = plainText + alpha[idx]
    return plainText

def substitutionEncryptNoSpaces(plainText, key):
    '''
    define substitution encryption function, take input of plain text, and a key, uses "alpha" variable for alphabet defined at the top of the file, removes spaces
    '''
    plainText = plainText.replace(" ", "")
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alpha.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText

def removeDupes(string):
    '''
    textbook issued function, i'm not writing docstrings for this, sorry not happening
    '''
    newString = ""
    for ch in string:
        if ch not in newString:
            newString = newString + ch
    return newString

def removeMatches(myString, removeString):
    '''
    textbook issued functions
    '''
    newString = ""
    for ch in myString:
        if ch not in removeString:
            newString = newString + ch
    return newString

def genKeyFromPass(password):
    '''
    textbook issued function
    '''
    key = alpha
    password = removeDupes(password)
    lastChar = password[-1]
    lastIdx = key.find(lastChar)
    afterString = removeMatches(key[lastIdx+1:], password)
    beforeString = removeMatches(key[:lastIdx], password)
    key = password + afterString + beforeString
    return key

def substitutionEncryptPassword(plainText, password):
    '''
    define substitution encryption function, take input of plain text, and a key, uses "alpha" variable for alphabet defined at the top of the file
    '''
    key = genKeyFromPass(password)
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alpha.find(ch)
        cipherText = cipherText + key[idx]
    print(password, key)
    return cipherText
