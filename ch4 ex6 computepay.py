# Excercise 6, Ch. 4 Pg. 55, Python For Informatics v3

# "Rewrite your pay computation with time-and-a-half for overtime and
# create a function called computepay which takes two parameters (hours and rate)"

inputloop = True
while inputloop is True:
    try:
        hours = float(input("Enter hours:"))
        rate = float(input("Enter pay rate per hour:"))
        if hours <= 0 or rate <= 0:
            print("Both hour & rate values entered must be above 0 to calculate pay.")
            continue
        # For future commits: There is a better way to obtain and parse user input.
        running = False
        break
    except:
        print("Please enter a numerical value for hours/rate.")

def computepay (hours, rate):
    if hours > 40:
        othours = hours - 40
        otrate = (rate * 1.5)
        otpay = othours * otrate
        pay = ((hours - othours) * (rate)) + otpay
    elif hours <= 40:
        pay = hours * rate
    pay = round(pay, 2)     #moved round(), str() conversion, and strip() into func.
    pay = str(pay).strip()
    return pay

print("Pay : $" + computepay(hours,rate))

## To implement:
    # If final pay beyond 0.00x decimal place, round up if >= 5 [DONE]
        # Round down if <5, though. [DONE - should work with round() function]
        # Can be accomplished with  print(round(computepay(hours, rate)2))
            #But how can I calcuate this myself (If I wanted to?)
    # Functions: Automatic deduction of 30 minutes meal time per day for 7.5+ shift
        #more precision needed for daily entry of hours (in order to accurately calculate
## Bugs:
    # Final pay output formatting (when no cents/when only cents in decimal place)
    # location of dollar sign [FIXED]

## Not implmented yet:
    # Compliance: https://www.dol.gov/whd/regs/compliance/whdfs53.htm
    # employee time from 1 to 7 minutes may be rounded down
    # employee time from 8 to 14 minutes must be rounded up
    # Potential to have the inputloop section be a defined function?
        # What about multiple inputs? How would that be handled?
        # A better/multiple input function is needed for more complex calcuations

### Test inputloop function based on observation of program flow:

# def inputloop (prompt,type):
#     #user input is returned
#     #prompt is string prompt for input
#     #type can be int, float, str
#     inputswitch = True
#     while inputswitch is True:
#         try:
#             if type == int:
#                 testinput = int(input(prompt))
#                 return testinput
#                 break
#             elif type == float:
#                 testinput = float(input(prompt))
#                 return testinput
#                 break
#             elif type == str:
#                 testinput = str(input(prompt))
#                 return testinput
#                 break
#         except:
#             print()