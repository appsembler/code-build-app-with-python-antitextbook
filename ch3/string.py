# -*- coding: utf-8 -*-
i = r'ßßßßßß  first string\n \tc \t c\tc'
print(i)
print(id(i))
j = "Wie heißen Sie?"

print(j)
k = """ third '''''""'
string"""

l = '''fourth
string'''

# print(i,j,k,l)

i = i + " added part" # IMMUTABLE
print(id(i))

print("-abcs-"*5)

print(i)
