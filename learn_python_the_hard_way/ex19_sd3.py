#ex.19, p.96,  Functions and Variables
#sd3:
# Write at least one more function of your own design, 
# and run it 10 different ways.
from sys import argv

def cu_func(paramA,paramB):
    print(f"Parameter A: {paramA}")
    print(f"Parameter B: {paramB}")
    print(f"Parameter A + B: {paramA + paramB}")

#1
cu_func(1,2)
#2
a = 2
b = 3
cu_func(a,b)
#3
input_a = int(input("Enter a"))
input_b = int(input("Enter a"))
cu_func(input_a,input_b)

#4
# argv for runtime parameters

#5
# from external file

#6
#7
#8
#9
#10


