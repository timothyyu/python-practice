# Exercise 1: Write a while loop that starts at the last character in the string and
# works its way backwards to the first character in the string, printing each letter on
# a separate line, except backwards.

teststring = "This is a test string"

#as a function (not currently working)
def printreverse(s):
    index = len(s) - 1
    count = 0
    while count < len(s):
        print(s[index])
        index = index - 1
        count = count + 1
#print(printreverse(teststring))

# Not as a function:
index = len(teststring) - 1
count = 0
while count < len(teststring):
    print(teststring[index])
    index = index - 1
    count = count + 1