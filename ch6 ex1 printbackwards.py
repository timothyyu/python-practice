# Exercise 1: Write a while loop that starts at the last character in the string and
# works its way backwards to the first character in the string, printing each letter on
# a separate line, except backwards.

teststring = "This is a test string"

# def printreverse(s):
#    while index < len(s):
#        index = index + 1
#        letter = s[index]
#    return letter
#
# print(printreverse(teststring))

#print (teststring[20]) #0-20 is range

# index = 0
# while index < len(teststring):
#     letter = teststring[index]
#     index = index + 1
#     print(letter)


index = len(teststring) - 1
count = 0
while count < len(teststring):
    print (teststring[index])
    index = index -1
    count = count + 1

