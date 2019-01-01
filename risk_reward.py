# 3. "Find something you need to calculate and write a new .py file that does it." p. 44

### Risk reward calc with enter-size-exit-stop ###

print("Enter values seperated via space:")
print("enter, exit, stop")

enter, exit, stop = input().split()

### Unit test - placeholders for enter, exit, stop testing ##

### Long test ###
#enter, exit, stop = 123,160, 75 
# exit test
#enter, exit, stop = 123,267, 75 
# stop test
#enter, exit, stop = 123,160, 111

### Short test ###
#enter, exit, stop = 3676.0, 3476.0, 3818.0 
# exit test
#enter, exit, stop = 3676.0, 3250.0, 3818.0 
# stop test
#enter, exit, stop = 3676.0, 3476.0, 3742.66 
print("Values entered for enter, exit, stop:")
print(enter, exit, stop ,"\n")

if exit > enter:
    print("Order Type: LONG")
elif exit < enter:
    print("Order Type: SHORT")
    
# Reverse map for conversion of spaced-sep inputs back to variable assignment
enter, exit, stop = list(map(float,[enter, exit, stop]))

print("Enter:", enter)
print("Exit: ", exit)
print("Stop: ", stop)

pt =  abs((exit-enter)/ (enter))
sl = abs((stop-enter)/ (enter)) 
pt_p = pt * 100
sl_p = sl * 100
rr = pt_p/sl_p
#print("pt,sl, pt/sl:",pt,sl,pt/sl)
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
        new_stop = abs(((enter *(pt/3.0))-enter))
        print("new stop to have RR of 3:")
        print(new_stop)
        
# removed order size parameter (for now) - optional pass parameter (later)
# https://www.bitmex.com/app/orderTypeFAQ
# https://www.bitmex.com/app/fairPriceMarking
# https://www.bitmex.com/app/pnlGuide#Example-4-Realised-PNL-Accounting

