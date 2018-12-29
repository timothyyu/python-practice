# 3. "Find something you need to calculate and write a new .py file that does it." p. 44

# Risk reward calc with enter-size-exit-stop

print("Enter values seperated via space:")
print("enter, exit, stop")

#enter, exit, stop = input().split()

# Test placeholder for enter, exit, stop
#enter, exit, stop = 123, 2, 160, 115 
enter, exit, stop = 3676.0, 3476.0, 3818.0 

print(enter, exit, stop ,"\n")

if exit > enter:
    print("Order Type: LONG")
elif exit < enter:
    print("Order Type: SHORT")
# Reverse map for conversion of spaced-sep inputs back to variable assignment
enter, exit, stop = list(map(float,[enter, exit, stop]))

print("Enter:", enter)
print("Exit: ", exit)
#print("Size: ", size)
print("Stop: ",stop)

pt_p = abs((exit-enter )/ (enter) * 100)
sl_p = abs((stop-enter )/ (enter) * 100)
rr = pt_p/sl_p
    
print("Exit:  {:.2f} %".format(pt_p))
print("SL:    {:.2f} %".format(sl_p))

print("RR:    {:.2f}".format(rr))


#removed order size parameter (for now) - optional pass parameter (later)

#https://www.bitmex.com/app/orderTypeFAQ
#https://www.bitmex.com/app/fairPriceMarking
#https://www.bitmex.com/app/pnlGuide#Example-4-Realised-PNL-Accounting

