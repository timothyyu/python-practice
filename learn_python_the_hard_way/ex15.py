#p.80 ex15 reading files
# run script with ex15_sample.txt argv parameter 

# Import argv function from sys module
from sys import argv

#argv and/or input() used to open ex15_sample.txt instead of hardcoding it in 
# script and filename argv input parameters at runtime
script, filename = argv

# Create filename object and open filename specified by argv
txt = open(filename)

# print name of filename object
print(f"Here's your file {filename}:")
# read in characters from filename object
print(txt.read())
# close file object
txt.close()

print("Type the filename again: ")
# use input() instead of argv to specify file name 
file_again = input("> ")
# create filename object and open filename specified by input()

txt_again = open(file_again)
# read in characters from filename object
print(txt_again.read())
# close file object
txt_again.close()