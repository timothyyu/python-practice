# 10.2 Write a program to read through the mbox-short.txt
#  and figure out the distribution by hour of the day for
# each of the messages. You can pull the hour out from the
#  'From ' line by finding the time and then splitting the
# string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print
#  out the counts, sorted by hour as shown below.
#
#desired output:
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
l = list()
d = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith("From "):
        words = line.split()
        #print words[5] #checking to see if this is part of string with time
        hours = words[5].split(':')
        #print hours[0] #checking to see if I have selected right part of 2nd split
        d[hours[0]] = d.get(hours[0],0) +1
for val, key in d.items():
    l.append((val,key))
l.sort()
#I had to look at the worked excercise in order to understand what I was doing
#...and EVEN THEN I DONT FULLY UNDERSTAND THIS D:
#Note: please lookup python documentation on this later
for val,key in l:
    print val, key








