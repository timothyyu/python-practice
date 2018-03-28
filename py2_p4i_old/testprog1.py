#beginning test 
print 'hello world'
lol = 3
hw = "hello world printed from variable"
no3 = "and the number"
print hw,no3,lol
#variable = <-----WHAT YOU DOIN FAM
x = 43
x = x+1 
print x
print "what kind of type is the above number?"
print "the number",x,"is a" 
print type(x)
#type function to check what type a value has
#str, int, float
a1 = ("17") 
print "checking the type of a number as represnted as a string:"
print type(a1)
#above is value 17 is a number, but represented as a string
#convert string to int/float to use in operations

#commas are used to represent a sequence - do not use commas. you might 
    #have to strip when dealing with parsing files and inputs that are not sanitized
print 1,000,000
print 1000000

#legal variable characters: underscore _, captials CAPS
    #illegal variable conventions: can not start variable name with number
print "example of illegal variable name 3variable. correct: threevariable"
#KNOW YOUR RESERVED KEYWORDS:
    # and as if assert break 
    # class continue def
    # del elif else except 
    # exec finally for from global 
    # if import in is lambda 
    # not or pass print raise 
    # while with yield
print "time for some OPERATIONS FAM"
#operators +, -, *, /, and **
    #DONT FORGET YO PEMDAS (ORDER OF OPERATIONS FAM)
minute = 59
minute = minute/60
print "minute/60 using floor division:"
print minute #result is zero ---> int divided by int will result in an interger
#aka answer is truncated to zero
print "remember fam, if either of the operands is a floating point, floating point division is performed"

#modulus
    #works on int only
    #gets the remainder
    #uses %
quotient = 7/3
remainder = 7%3
print "7/3 with %: (int division)"
print quotient
print "7/3 with /:"
print remainder

#operations fam 
    # + plus operator concatenates (joins) strings by linking them end to end
x = "ayyy"
y = "lmaooo"
print "concatenation of two strings:"
print x+y

first = "100"
second = "150"
print first+second
#can then further convert that into a float/int 

#asking for user input 
    #raw_input
    #raw input takes what the user types as a string

##print "enter text for raw input:"
#input = raw_input()
#print "what you entered was " + input

#another way to do this
    #name = raw_input('WHAT YO NAME FAM \n')
    #\n new line break
    #print name

#converting values to int using int()
    #prompt = "how fast you moving fam? \n"
    #speed = raw_input(prompt)
        #can put string question where prompt is here fam
    #print int(speed)
    
#last section left off is 2.11 comments page 25/26

#which of the following are reserved words?
    #for word in words:
        #print word
    #for slice in pizza:
        #print slice

#last section 3.11