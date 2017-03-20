# Python programming challenge:
# Write a program that can take input
# in the form of WHOLE integers 1 to 1000, and outputs them as words

inputloop = True
isNegative = None
while inputloop is True:
    try:
        wholeint = input("Enter a whole integer between 1 and 1000:")
        wholeint = int(wholeint)
        if wholeint > 1000:
            print ("Entered INT is >1000. Please Try again.")
            continue
        elif wholeint < -1000:
            print("Entered INT is <-1000. Please Try again.")
            continue
        if wholeint <0:
            isNegative = True
            wholeint = abs(wholeint)
        elif wholeint >0:
            isNegative = False
        running = False
        break
    except ValueError:
        print ("ERROR: You did not enter a whole int")
        print ("Please try again:")

if isNegative == True:
    # convert to string to get negative sign right next to number
    # Use temp variable to not disrupt program flow
    tempwholeint = str(wholeint)
    print("Whole INT entered succesfully.\nYou entered:","-"+ tempwholeint)
elif isNegative == False:
    print("Whole INT entered succesfully.\nYou entered:",  wholeint)

###############################################

dict1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty',
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty',
            90: 'Ninety', 0: 'Zero',}
dict2 = { 100:'Hundred', 1000: 'Thousand',}

###############################################

def round_down(num, divisor):
    return num - (num%divisor)
def under100 (wholeint):
    # ex47
    # x = the number under 99 minus the tens place
    # 40 and 7 --> 47 round down to 40 which will be x
    # need function to round down to 10
    x = round_down(wholeint,10)
    wholeintm = wholeint - x
    if x <= 0:
        numword = dict1[wholeintm]
    elif wholeintm == 0:
        numword = dict1[x]
    elif x > 0:
        numword = dict1[x] + '-' + dict1[wholeintm]
    return numword

def above101(wholeint):
    # ex 451
    x = round_down(wholeint, 100)
    y = x/100
    tensleft = wholeint - x
    if tensleft == 0:
        numword = dict1[y] + " " + dict2[100]
    else:
        numword = dict1[y] +" "+ dict2[100] +" and " + under100(tensleft)
    return numword

###############################################

if wholeint == 1000:
    numword = dict1[1]+ " "+ dict2[wholeint]
elif wholeint >= 101:
    numword = above101(wholeint)
elif wholeint == 100:
    numword = dict1[1] +" " + dict2[wholeint]
elif wholeint <20 or wholeint <=99 and not wholeint >=21:
    numword = dict1[wholeint]
elif wholeint >=21:
    numword= under100(wholeint)

#Commented out swath of if/elif that is replaced by the above
# if wholeint <= 99:
#     if wholeint <20:
#         numword = dict1[wholeint]
#     elif wholeint == 20:
#         numword = dict1[wholeint]
#     elif wholeint == 30:
#         numword = dict1[wholeint]
#     elif wholeint == 40:
#         numword = dict1[wholeint]
#     elif wholeint == 50:
#         numword = dict1[wholeint]
#     elif wholeint == 60:
#         numword = dict1[wholeint]
#     elif wholeint == 70:
#         numword = dict1[wholeint]
#     elif wholeint == 80:
#         numword = dict1[wholeint]
#     elif wholeint == 90:
#         numword = dict1[wholeint]

# isNegative flag and abs() function to add "Negative" to negative input print statement
if isNegative == True:
    print("Number in written form:"," Negative", numword)
elif isNegative == False:
    print("Number in written form:", numword)

#To implement:
    # design for -1 and negative input [DONE]
    # rewrite definitions to be easier to understand
    # see if there a better way to structure control logic starting with
        # if wholeint <= 99:
    # Change output to be more readable, i.e. 100 in written form is x
    # You entered statement negative symbol added [DONE]
    # Control flow idea: use a for/while loop for wholeint <= 99

# Issues:
    # Final output has a space/few extra spaces left side of "You Entered:" [FIXED]
    # -1000 output error: Entered INT is <-1000. Please Try again. [FIXED]
    # negative input not showing in "you entered" [FIXED]
    # "You entered:" output by convert to string (placed in temp variable) [FIXED]
    # Updated comments on lower program flow
    # Print statement left space "You Entered" [FIXED]


