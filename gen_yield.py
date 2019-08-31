def myGenerator(stopValue):
    choke = 0
    while choke < stopValue:
        yield choke * 2
        choke += 1
g = myGenerator(6)
for item in g:
    print(item)