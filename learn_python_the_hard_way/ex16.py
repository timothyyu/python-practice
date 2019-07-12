#ex16 p.84 reading and writing files

from sys import argv
script,filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")

# 'w' flag = open for writing, truncating the file first
target = open(filename,'w')
print ("Truncating the file. Goodbye!")
# truncate() ---> empties the file, regardless of the existing content
target.truncate()
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

#writes the input() line content into the new file, seperated by a new line
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

target.write(line1 + "\n" + line2 +"\n" +  line3 + "\n")
print("And finally, we close it.")
# closes the file
target.close()
