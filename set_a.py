#!/usr/bin/env python3
#
# p. 89
#

"""
3.1 Create a string variable that is initialized to your entire name -
first, middle, and last.
"""
name = "Alex Forrester"


"""
3.2 Using the slice operator, print your first name.
"""
print(name[0:4])


"""
3.3 Using the slice operator, print your last name.
"""
print(name[5:14])


"""
3.4 Using the slice and concatenation operators, print your name in the
form "Lastname, Firstname."
"""
print(name[5:14] + ", " + name[0:4])


"""
3.5 Print the length of your first name.
"""

print(len(name[0:4]))

"""
3.6 Assume you have two variables: `s='s'`, and `p='p'`. Using
concatenation and repetition, write an expression that produces the
string 'mississippi'.
"""
s = "s"
p = "p"
print("mi" + s*2 + "i" + s*2 + "i" + p*2 + "i")


"""
3.7 Modify the prefix example in Session 3.5 to print all prefixes of
"Roy G Biv," including the entire string.
"""
RGB = "Roy G Biv"
for i in range(len(RGB)+1):
    print(RGB[0:i])
