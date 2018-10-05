# import regular expression library - library not built in/imported by default
import re

x = "This is an example string"
y = "This is an example string :"
z = "This-is-an: example string @"

if re.search('is',x):
    print("is 'is in string x")

# ^ is for match at beginning of line
if re.search('^This',x):
    print("^This = True")
    
if re.search('^T.*:',y):
    print("Matches start of line, match any character, has a colon")
if re.search('^T\S+:',z):
    print("Match start up line, match any non-whitespace character 1 or more times up to colon")

numstring = "This is This 1 2, 3, 3, 5, 6,7,8,9"
numfound = re.findall('[0-9]+',numstring)
print(numfound)