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
# The results will be slightly more accurate than atSymbolNumChar/re07.py for email address
def atSymbolNumCharAcc(file):
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
    # New Python 3.x way to print list elements on new lines 
        # requires from __future__ import print_function 
    print(*matset_l,sep='\n')

# Remove email addresses that start with a number
# and have a period 13 characters in
#for item in matset_l:
    #if item[0][0].isdigit() and item[0][12] == '.':
        #print(item)
        #matset_l.del(item)

# Search for lines that start 'X' followed by any non whitespace
# characters and ':' then output the first group of non whitespace
# characters that follows
def xNonWhiteSpace(file):
    hand = open(file)
    for line in hand:
        line = line.rstrip()
        x = re.findall('^X\S*: (\S+)', line)
        if not x: continue
        print(x)

# Search for lines that start with 'X' followed by any non
# whitespace characters and ':'
# followed by a space and any number.
# The number can include a decimal.
# For sample file mbox-short.txt, this outputs the X-DSPAM-Probality and confidence:
def xNWSnumCharFollow(file):
    hand = open(file)
    for line in hand:
        line = line.rstrip()
        if re.search('^X\S*: [0-9.]+', line):
            print(line)

# Search for lines that start with 'X' followed by any
# non whitespace characters and ':' followed by a space
# and any number. The number can include a decimal.
# Then print the number if it is greater than zero.
# For sample file mbox-short.txt, this outputs the same numeric portion of the above
def xNWSnumCharFollowZero(file):
    hand = open(file)
    for line in hand:
        line = line.rstrip()
        x = re.findall('^X\S*: ([0-9.]+)', line)
        if len(x) > 0:
            print(x)

##########################################################

### Main function calls for regex functions ###
xNWSnumCharFollowZero(file)
#xNWSnumCharFollow(file)
#xNonWhiteSpace(file)
#atSymbolNumCharAcc(file)
#atSymbolNumChar(file)
#atSymbol(file)
#fromLines(file)

##########################################################

### TODO ###

# Filter output one space after 'From:' (as new function, or extension of existing function)
    # Another function extension that uses set functionality to remove duplicates
        # Using list ---> tuple ----> set ---> list
            # list items are unordered/mutable, tuples are immutable
            # can't create set from list of lists (output of l is list of lists)
        # Using list, loop to not add item if already in list (checks if already in list/unique)
        # Using OrderedDict
        
# Go through re012.py - re15.py examples