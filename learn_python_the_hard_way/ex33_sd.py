"""
# p.146, excercise 33, "While Loops" (Learn Python The Hard Way)

"""

def while_loop_func(limit, increment):
    i = 0
    numbers = []

    while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom is is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)
# while_loop_func(6,2)

# A for-loop can only iterate (loop) ”over” collections of things.
# A while-loop can do any kind of iteration (looping) you want.

def while_loop_func2(limit, increment):
    i = 0
    numbers = []
    for i in range(0, limit):
    #while i < limit:
        print(f"At the top i is {i}")
        numbers.append(i)
        #i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom is is {i}")


    print("The numbers: ")

    for num in numbers:
        print(num)



while_loop_func2(6,2)



    
