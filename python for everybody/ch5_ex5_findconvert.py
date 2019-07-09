# Excercise 5, Ch. 6 Pg. 69, Python For Informatics v3

# Exercise 5: Take the following Python code that stores a string:‘
# str = ’X-DSPAM-Confidence:0.8475’
# Use find and string slicing to extract the portion of the string after the colon
# character and then use the float function to convert the extracted string into a
# floating point number.

str1 = 'X-DSPAM-Confidence:0.8475'
slice1 = str1[(len(str1)-6):]
slice1float =float(slice1)

print ("Is the converted string a float:")
if type(slice1float) == float:
    print ("Yes")
elif type(slice1float) is not float:
    print ("Converted string is not float")

print ("Sliced and converted string: %s" %slice1float)