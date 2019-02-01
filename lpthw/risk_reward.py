# 3. "Find something you need to calculate and write a new .py file that does it." p. 44

### Risk reward calc with enter-exit-stop ###

print("Enter values seperated via space:")
print("enter, exit, stop")

#enter, exit, stop = input().split()

### Unit test - placeholders for enter, exit, stop testing ##
### Long test ###
## exit test
#enter, exit, stop = 123, 160, 75 
# stop test
enter, exit, stop = 123, 160, 111

### Short test ###
#enter, exit, stop = 3676.0, 3476.0, 3818.0 
# exit test
#enter, exit, stop = 3676.0, 3250.0, 3818.0 
# stop test
#enter, exit, stop = 3676.0, 3476.0, 3742.66 

print("Values entered for enter, exit, stop:")
print(enter, exit, stop ,"\n")
  
# Reverse map for conversion of spaced-sep inputs back to variable assignment
enter, exit, stop = list(map(float,[enter, exit, stop]))

reward =  abs((exit-enter)/ (enter))
risk = abs((stop-enter)/ (enter)) 
reward_p = reward * 100
risk_p = risk * 100

rr = abs((exit-enter)/(stop-enter))
# LONG: RR = (Exit - Enter) / (Enter - Stop)
# SHORT: RR = (Enter - Exit) / (Stop - Enter)

if exit > enter:
    print("Order Type: LONG")
elif exit < enter:
    print("Order Type: SHORT")
print("Enter:", enter)
print("Exit: ", exit)
print("Stop: ", stop)
print("Exit%: {:.2f} %".format(reward_p))
print("SL%:   {:.2f} %".format(risk_p))
print("RR:    {:.2f}".format(rr))

if (rr < 3):
    print("============")
    print("RR is not > 3!")
    #SHORT
    if enter > exit: 
        new_exit = abs((((3.0 * risk) * enter))-enter)
        print("new exit for RR of 3:")
        print(new_exit)
        new_stop = abs(((enter *(reward/3.0))+enter))
        print("new stop for RR of 3:")
        print(new_stop)
    #LONG
    if enter < exit:
        new_exit = abs((((3.0 * risk) * enter))+enter)
        print("new exit for RR of 3:")
        print(new_exit)
        new_stop = abs(((enter *(reward/3.0))-enter))
        print("new stop for RR of 3:")
        print(new_stop)

rrPass = False
target_rr = 5 
if rrPass is True:
    print(f"target_rr: {target_rr}")
    #SHORT
    if enter > exit: 
        new_exit = abs((((target_rr * risk) * enter))-enter)
        print(f"new exit for RR of {target_rr}:")
        print(new_exit)
        new_stop = abs(((enter *(reward/target_rr))+enter))
        print(f"new stop for RR of {target_rr}:")
        print(new_stop)
    #LONG
    if enter < exit:
        new_exit = abs((((target_rr * risk) * enter))+enter)
        print(f"new exit for RR of {target_rr}:")
        print(new_exit)
        new_stop = abs(((enter *(reward/target_rr))-enter))
        print(f"new stop for RR of {target_rr}:")
        print(new_stop)       
# removed order size parameter (for now) - optional pass parameter (later)
# https://www.bitmex.com/app/orderTypeFAQ
# https://www.bitmex.com/app/fairPriceMarking
# https://www.bitmex.com/app/pnlGuide#Example-4-Realised-PNL-Accounting

# Edgewonk Math Cheatsheet ref:
    # https://www.tradeciety.com/wp-content/uploads/Math.pdf
# Minimum Winrate = 1 / (1 + Reward:Risk)
    # historical winrate --> minimum reward:risk ratio
    # 25% --> 3:1
    # 33% --> 2:1
    # 40% --> 1.5:1
    # 60 --> 0.7:1
    # 75% --> 0.3:1
minimum_winrate = 1 / ( 1 + rr)
print("Minimum winrate: {:.2f}%".format(minimum_winrate*100 ))