hrsraw = raw_input("Enter Hours:")
hrs = float(hrsraw)
rateraw = raw_input("Enter Rate:")
rate = float(rateraw)

def computepay (hrs, rate):
    if hrs < 40 :
        gross = rate * hrs
    elif hrs > 40 :
        extragross = (hrs - 40) * (rate * 1.5)
        gross = rate * 40
        gross = extragross + gross
    return gross


p = computepay (hrs,rate)       
print p