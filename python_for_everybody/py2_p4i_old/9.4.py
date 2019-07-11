# 9.4 Write a program to read through the mbox-short.txt and
# figure out who has the sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of
# those lines as the person who sent the mail. The program creates
# a Python dictionary that maps the sender's'
# mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the
# dictionary using a maximum loop to find the most prolific committer.

name = raw_input("Enter file:")
# if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
d = dict()
for line in handle:
    line = line.rstrip()
    line.split()
    if line.startswith("From "):
        words = line.split()
        if words[1] not in d:
            d[words[1]]= 1
        else:
            d[words[1]] = d[words[1]] + 1
#print d
largestkey = 0
for key in d:
    #print key, d[key]
    if d[key] > largestkey:
        largestkey = d[key]

if key in d:
    print words[1], largestkey


