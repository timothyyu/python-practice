#Excercise 6, Ch. 4 Pg. 55, Python For Informatics v3

#"Rewrite your pay computation with time-and-a-half for overtime and
#create a function called computepay which takes two parameters (hours and rate)"

inputloop = True
while inputloop is True:
    try:
        hours = float(input("Enter hours:"))
        rate = float(input("Enter pay rate per hour:"))
        break
    except:
        print("Please enter a numerical value for hours/rate.")

def computepay (hours, rate):
    if hours > 40:
        othours = hours - 40
        otrate = (rate * 1.5)
        otpay = othours * otrate
        pay = ((hours - othours) * (rate)) + otpay
    elif hours < 40:
        pay = hours * rate
    return pay

print("Pay: $", round(computepay(hours, rate),2))

#Bugs/issues to be addressed in future versions:
    #Compliance: https://www.dol.gov/whd/regs/compliance/whdfs53.htm
        #employee time from 1 to 7 minutes may be rounded down
        #employee time from 8 to 14 minutes must be rounded up
    #Functions: Automatic deduction of 30 minutes meal time per day for 7.5+ shift
    #If final pay beyond 0.00x decimal place, round up if >= 5
        #Round down if <5, though.
        #!!!!!!!can be accomplished with  print(round(computepay(hours, rate)2))
            #But how can I calcuate this myself (If I wanted to?)
    #Final pay output formatting (when no cents/when only cents in decimal place
    #Potential to have the inputloop section be a defined function?
        #What about multiple inputs? How would that be handled?

###Test inputloop function based on observation of program flow:

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