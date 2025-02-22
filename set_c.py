#!/usr/bin/env python3
#
# pp. 99, 103
#
from encrypt_functions import *
"""
3.17 With paper and pencil, use the transposition algorithm to encrypt the
sentence "the quick brown fox jumps over the lazy dog."  Check your
answer by calling the `scramble2Decrypt` function.
"""
#TEQIKBONFXJMSOE H AYDGH UC RW O U P V R TELZ O
x=scramble2Encrypt("the quick brown fox jumps over the lazy dog")
print(scramble2Decrypt(x))

"""
3.18 Write a python function `stripSpaces(myString)` that takes a string
representing a phrase as a parameter and returns the paragraph with
the order of the letters intact but the spaces between each word
removed.
"""
def stripSpaces(myString):
    return(myString.replace(" ", ""))
print(stripSpaces("Tu madre es una persona"))

"""
3.19 The transposition cipher can be generalized to any number of rails.
Write a function to implement a three-rail fence cipher that takes
every third character and puts it on one of the three rails.
"""
print(non_binary_trans_cipher_encrypt("Circle"))
print(non_binary_trans_cipher_decrypt(non_binary_trans_cipher_encrypt('Circle')))

"""
3.20 Make up your own key and encrypt a message. Exchange your key and the
ciphertext with a partner to see if you can decrypt each other's
message.
"""



"""
3.21 Write the `substitutionDecrypt` method.
"""
key1 = "ouwckbjmpzyexavrltsfgdqihn "
cipherTextTest = substitutionEncrypt("Finn wants to go to Dr Bennits office",key1)
print(cipherTextTest)
plainTextTest = substitutionDecrypt(cipherTextTest, key1)
print(plainTextTest)


"""
3.22 Rewrite the `substitutionEncrypt` function, but remove all spaces
from the plaintext message.
"""
key1 = "ouwckbjmpzyexavrltsfgdqihn "
cipherTextTest = substitutionEncryptNoSpaces("Finn wants to go to Dr Bennits office",key1)
print(cipherTextTest)
plainTextTest = substitutionDecrypt(cipherTextTest, key1)
print(plainTextTest)
