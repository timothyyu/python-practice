#ex.20, p100,  Functions and Files

# Module import for argv input at command line level input
from sys import argv
# Specifying list order for input parameters at command line level input at runtime
# input_file is the file that you specify
script, input_file = argv

# Function to read entire file and print contents
def print_all(f):
    print(f.read())
# Function to move demarker/marker to beginning of the file
    # We understand this as a sequential rewind if we're using analog terms and analogies
def rewind(f):
    # .seek moves to start of stream
    f.seek(0)

# Function to print the current line + the contents of said line
def print_a_line(line_count,f):
    print(line_count,f.readline())

# file specified in command line/runtime argv is opened
current_file=open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line,current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)