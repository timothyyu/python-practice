# Excercise 1, Ch. 5 Pg. 65, Python For Informatics v3

# Write a program which repeatedly reads numbers until the user enters
# “done”. Once “done” is entered, print out the total, count, and average of the
# numbers. If the user enters anything other than a number, detect their mistake
# using try and except and print an error message and skip to the next number.

lst = []
inputloop = True
while inputloop is True:
    try:
        number=input("Enter a number:")
        if number == "done" or number == "Done":
            break
        number = int(number)
        lst.append(number)
    except ValueError:
        print("Invalid input")
        continue
avg = sum(lst) / len(lst)
print ("Numbers entered: ", lst)
print ("Sum, count of numbers entered, average: ", sum(lst),",",len(lst),",", avg) # sum, number of inputs, average

