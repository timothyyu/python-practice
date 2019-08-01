#Unicode characters and strings

#1960s/1970s ---> we assumed one byte is one character and went it with
    # a byte and character were assumed to be the same thing
    #ASCII goes up to 127

print(ord('H'))
print(ord('e'))
print(ord('\n'))
print(ord('G'))

#UTF-16 - fixed length, two byes
#UTF-32 - fixed length, four byes
#UTF-8 - 1-4 bytes
    # upwards compat with ASCII
    # auto detection between ASCII & UTF-8
    # UTF-8 rec best pracetice for encoding/data exchange between systems

# in python3, all strings are unicode

# data in from external resource
    # must be decoded based on its character set so it's properly represented in py3 as a string
    # when talking to external network resource that sends bytes,
        # you need to encode the py3 strings into a given char encoding