largest = None
smallest = None

while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
        num = int(num)
    except:
        print "Invalid input"
        continue
    if smallest is None:
        #this is to make sure there are values for both
        #smallest and largest
        #i don't think that you can compare a value
        #directly to None?
        smallest = num
        largest = num
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num


print "Maximum is", largest
print "Minimum is", smallest