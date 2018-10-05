# Python regular expressions

# Import regular expression library
import re


# regular expressions --> programming with characters instead of lines
    # another definition: a programming language for string matchng (inside of python)

# Load in source text file from sample source code directory
file = 'py3_p4e_sample_code/mbox-short.txt'   

# Regex functions
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

def atSymbol(file):
    hand = open(file)
    for line in hand:
        x = re.findall('\S+@\S+', line)
            #'\S' matches any non-whitespace character
            #'+' Repeats a character one or more times (greedy)
        if len(x) > 0:
            print(x)

fromLines(file)
#atSymbol(file)

# TODO
    # Filter output one space after 'From:' (as new function, or extension of existing function)
        # Another function extension that uses set functionality to remove duplicates
        # Same as above, but preserving order using OrderedDict()
    # Function --> Function call: Load in file via function-function call
