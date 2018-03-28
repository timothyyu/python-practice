fname = raw_input("Enter File Name: ")
#filename mbox-short.txt
fh = open(fname)
count = 0
for line in fh:
    line = line.rstrip()
    line.split()
    #if not line.startswith("From:"):
        #if line.startswith("From "):
    if not line.startswith("From:") and line.startswith("From "):
        words = line.split()
        count = count + 1
        print words[1]


print "There were", count, "lines in the file with From as the first word"
