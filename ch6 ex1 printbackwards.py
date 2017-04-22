# Exercise 1: Write a while loop that starts at the last character in the string and
# works its way backwards to the first character in the string, printing each letter on
# a separate line, except backwards.

teststring = "This is a test string"

def printreverse(s):
   while index < len(s):
       letter = s[index]
       index = index +1
   return letter

print(printreverse(teststring))