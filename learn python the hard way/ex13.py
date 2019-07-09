#pg.72 ex13 parameters, unpacking,variables

from sys import argv
#read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# run script from command line with:
    # python ex13.py first 2nd 3rd
    # you can pass anything you want for first/2nd/3rd