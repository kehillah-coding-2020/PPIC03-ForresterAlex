#!/usr/bin/env python3
#
# pp. 108, 113
#
from encrypt_functions import *
"""
3.23 Write the `removeChar` function using *for* loops rather than slice
operators.
"""
def removeChar(string, char):
    '''
    takes input of string and charecter to remove from string
    '''
    new_string = ''
    for i in string:
        if i != char:
            new_string = new_string + i
    return new_string
print(removeChar("hello", "l"))

"""
3.24 Modify the `removeChar` function so that it works for negative
character indexes.
"""
def removeChar(string, idx):
    '''
    takes input of string and index and returns string without index
    '''
    return string[:idx]

print(removeChar("hello",-1))
"""
3.25 Modify the `substitutionCipher` function to use the `genKeyFromPass`
function.
"""
print(substitutionEncryptPassword("finn really likes dr bennets office", "dr bennets office"))


"""
3.26* Encryption often involves the Caesar cipher - named after Julius
Casesar, who used the system to encrypt military messages. Many early
Internet users also adopted this cipher. Called `rot13`, the cipher
encrypts a message by rotating the plaintext character by 13
positions in the alphabet. For example, "a" becomes "n" and likewise
"n" becomes "a". The nice thing about `rot13` is that the same
function can be used to encrypt and decrypt a message. Write a
function called `rot13` that takes a message as a parameter and
rotates all the characters by 13 places.
"""



"""
3.27* Rewrite the Caesar cipher so that it takes the number of places to
rotate as a parameter. You will have to write separate encrypt and
decrypt functions.
"""



"""
3.28* Write a function `undoVig(keyLetter, ctLetter)` that takes a letter
from the key, a ciphertext letter, and returns the plaintext letter.
"""



"""
3.29* Writte a function `decryptVignere` that takes a keyword, the
ciphertext for the message, and returns the plaintext message.
"""
