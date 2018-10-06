### Python regular expressions ###

# Python 3.x print function import
from __future__ import print_function

# Import regular expression library
import re
# regular expressions --> programming with characters instead of lines
    # another definition: a programming language for string matchng (inside of python)

# Import for OrderedDict 
    # Under Python 3.6, built-in dict does track insertion order 
# from collections import OrderedDict 

##########################################################

# Load in source text file from sample source code directory
file = 'py3_p4e_sample_code/mbox-short.txt'   

### Regex functions examples ###

def fromLines(file):
    hand = open(file)
    for line in hand:
        line = line.rstrip()
        if re.search('^From:.+@', line):
            # Search for lines that contain 'From'
                # From:
            # Search for lines that start with 'From'
                # ^From:
            # Search for lines that start with 'F', followed by
            # 2 characters, followed by 'm:'
                # ^F..m: 
            # Search for lines that start with From and have an at sign
                # ^From:.+@
            print(line)

# Search for lines that have an at sign between characters
def atSymbol(file):
    hand = open(file)
    for line in hand:
        x = re.findall('\S+@\S+', line)
            #'\S' matches any non-whitespace character
            #'+' Repeats a character one or more times (greedy)
        if len(x) > 0:
            print(x)

# Search for lines that have an at sign between characters
# The characters must be a letter or number
def atSymbolNumChar(file):
    hand = open(file)
    for line in hand:
        line = line.rstrip()
        x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', line)
        if len(x) > 0:
            print(x)

##########################################################

# Create new list to hold unfiltered/raw results from regex expressions
l = list()

# Search for lines that have an at sign between characters
# The characters must be a letter or number
# The results will be slightly more accurate than re07.py for email addresses

# def atSymbolNumCharAcc():
hand = open(file)
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9\-.]\S+@[a-zA-Z0-9].\S+[a-zA-Z]', line)
    if len(x) > 0:
        #print(x)
        l.append(x)
#print(l)


# Lists are mutable = therefore not hashable
    # list ---> tuple ----> set ---> list
mat = [tuple(t) for t in l]
matset = set(mat)
matset_l= [list(t) for t in matset]
print(matset_l)

# New Python 3.x way to print list elements on new lines 
    # requires from __future__ import print_function 
print(*matset_l,sep='\n')

### Main function calls for regex funcaccess list valuestion expression tests ###

#fromLines(file)
#atSymbol(file)
#atSymbolNumChar(file)

##########################################################

### TODO ###

# Filter output one space after 'From:' (as new function, or extension of existing function)
    # Another function extension that uses set functionality to remove duplicates
        # Using list ---> tuple ----> set ---> list
            # list items are unordered/mutable, tuples are immutable
            # can't create set from list of lists (output of l is list of lists)
        # Using list, loop to not add item if already in list (checks if already in list/unique)
        # Using OrderedDict
        
# re09.py - re15.py examples