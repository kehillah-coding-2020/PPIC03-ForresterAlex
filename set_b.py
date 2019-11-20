#!/usr/bin/env python3
#
# pp. 91, 93
#
"""
3.8 Using the count method, find the number of occurrences of the
character 's' in the string 'mississippi'.
"""
string = 'mississippi'
print(string.count("i"))

"""
3.9 Replace all occurences of the substring 'iss' with 'ox'.
"""
print(string.replace('iss','ox'))


"""
3.10 Find the index of the first occurrence of 'p' in 'mississippi'.
"""
print(string.find('p'))


"""
3.11 Make the word 'python' centered and all capital letters in a string
of length 20.
"""
yarn = "python"
yarnU = yarn.upper()
print(yarnU.center(20))

"""
3.12 What is the difference between `ord('A')` and `ord('a')`?
"""
print(ord('A'))
print(ord('a'))
'''
the difference is due to the fact that 'A' and 'a' equal different numbers in ASCII"
'''

"""
3.13 Write a function that takes a single character digit and returns its
integer value, using only the `ord()` function.
"""
def intvalue(letter):
    return(ord(letter))

print(intvalue("A"))
"""
3.14 Write the `letterToIndex` function using `ord` and `chr`.
"""
def letterToIndex(letter):
    return(ord(letter)-64)
print(letterToIndex("A"))


"""
3.15 Write the `indexToLetter function using `ord` and `chr`.
"""
def indexToLetter(index):
    return(chr(index+64))
print(indexToLetter(1))


"""
3.16 Write a function that takes an exam score from 0-100 and returns the
corresponding letter grade.
"""
