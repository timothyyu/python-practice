#pg.72 ex13 parameters, unpacking,variables
#sd3 combine input with aargv to make a script that gets more input from the user

from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

a1 = input("Parameter A1:")
a2 = input("Parameter A2:")

print(f"Parameter A1 is {a1}, parameter A2 is {a2}")
