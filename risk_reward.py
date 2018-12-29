# 3. "Find something you need to calculate and write a new .py file that does it." p. 44

# Risk reward calc with enter-size-exit-stop

print("Enter values seperated via space:")
print("enter, exit, stop")

#enter, exit, stop = input().split()

# Test placeholder for enter, exit, stop
#enter, exit, stop = 123,160, 75 

enter, exit, stop = 3676.0, 3476.0, 3818.0 
#enter, exit, stop = 3676.0, 4102.0, 3818.0 
    # works
#enter, exit, stop = 3676.0, 3476.0, 3760.0 

#enter, exit, stop = 3676.0, 3250.0, 3610.0
#enter, exit, stop = 3676.0, 3250.0, 3742.66 
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

pt =  abs((exit-enter)/ (enter))
sl = abs((stop-enter)/ (enter)) 
pt_p = pt * 100
sl_p = sl * 100

#print("pt,sl, pt/sl:",pt,sl,pt/sl)

rr = pt_p/sl_p
    
print("Exit%: {:.2f} %".format(pt_p))
print("SL%:   {:.2f} %".format(sl_p))

print("RR:    {:.2f}".format(rr))

if (rr <= 3):
    #SHORT
    if enter > exit:
        print("RR is not > 3!")
        new_exit = abs((((3.0 * sl) * enter))-enter)
        print("new exit to have RR of 3:")
        print(new_exit)
        new_stop = abs(((enter *(pt/3.0))+enter))
        print("new stop to have RR of 3:")
        print(new_stop)
    #LONG
    if enter < exit:
        print("RR is not > 3!")
        new_exit = abs((((3.0 * sl) * enter))+enter)
        print("new exit to have RR of 3:")
        print(new_exit)
        new_stop = abs(((enter *(pt/3.0))+enter))
        print("new stop to have RR of 3:")
        print(new_stop)
#removed order size parameter (for now) - optional pass parameter (later)

#https://www.bitmex.com/app/orderTypeFAQ
#https://www.bitmex.com/app/fairPriceMarking
#https://www.bitmex.com/app/pnlGuide#Example-4-Realised-PNL-Accounting

