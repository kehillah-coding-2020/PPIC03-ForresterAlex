#common functions for Encryption and Decryption

def scramble2Decrypt(cipherText):
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
    string_len = len(string)
    third_len = len(string)//3
    output = ''
    for i in range(third_len):
        temp = i * 3
        output = output + string[temp] + string[temp-1] + string[temp-2]
    return(output)
