#boolean expression = either true or false
#print 10 == 2
#print 2 == 2

# comparision operators
# ==
# =!
# >, <, <=, >=
# is        a is the same as b
# is not    a is not the same as b

#three logical operators: ando, or, not
print "not operator test"
x = 1
y = 2
print not (x == y)

#x == y is false, but not (x ==y) is true

#or = if either of the conditions is true
#and = if both conditions true

print x == 1 and not y == 1
# x == 1 is true, y ==1 is false, but not(y==1) is true

#for chained conditionals: even if more than one condition true,
# only the first branch executes
#avoid nested conditionals if you can - they are harder to read

#logical operators can simplfly nested conditionals:
a=1
if 0 < a:
    if a < 10:
        print "a is a postive single digit number"
# can be written like this (print statement only happens if both conditionals are satisified:
if 0 < a and x < 10:
    print "a is a postive single digit number"