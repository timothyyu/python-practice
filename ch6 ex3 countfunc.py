# Excercise 6, Ch. 6 Pg. 70, Python For Informatics v3
#Encapsulate a looping program that counts the number of times
# a specified letter appears in a string into a function (and accepts the string and letter as arguments)

def count(str, let):
    count = 0
    for letter in str:
        if letter == let:
            count = count + 1
    print(count)

count("banana",'a')