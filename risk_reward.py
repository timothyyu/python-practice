# 3. "Find something you need to calculate and write a new .py file that does it." p. 44

# Risk reward calc with enter-size-exit-stop

print("Enter values seperated via space:")
print("enter, size, exit, stoploss")

#enter, size, exit, stop = input().split()

# Test placeholder for enter, size, exit, stoploss
#enter, size, exit, stop = 123, 2, 160, 115 
enter, size, exit, stop = 3676.0, 1, 3476.0, 3818.0 

print(enter, size, exit, stop)
# Reverse map for conversion of spaced-sep inputs back to variable assignment
enter, size, exit, stop = list(map(float,[enter, size, exit, stop]))

print("Enter:", enter)
print("Exit: ", exit)
print("Size: ", size)
print("Stop: ",stop)

pt_p = abs((exit-enter )/ (enter) * 100)
sl_p = abs((stop-enter )/ (enter) * 100)
rr = pt_p/sl_p

print("Exit%: {:.2f}".format(pt_p))
print("SL%:   {:.2f}".format(sl_p))

print("RR:    {:.2f}".format(rr))



#https://www.bitmex.com/app/orderTypeFAQ
#https://www.bitmex.com/app/fairPriceMarking
#https://www.bitmex.com/app/pnlGuide#Example-4-Realised-PNL-Accounting
