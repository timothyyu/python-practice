# Examples of tabbed list, inline new line char, and escape sequence test


# Tabbed list example output

tlist= """
\t * item 1
\t * item 2
\t * item 3 """

print("This is a tabbed list:", tlist)
#print()

print("Split line after THIS,\nthe above is on it's own line")

print("This is a backslash in python: \\")

formatter = "\t{} \t \t{} \t \t {} \t \t{}"
print(formatter.format(1,2,3,4))