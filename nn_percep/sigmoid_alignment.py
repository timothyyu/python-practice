# # https://www.geeksforgeeks.org/implement-sigmoid-function-using-numpy/
import copy
import numpy as np
np.random.seed(0)

# compute sigmoid nonlinearity
def sigmoid(x):
    output = 1/(1+np.exp(-x))
    return output

# convert output of sigmoid function to its derivative
def sigmoid_output_to_derivative(output):
    return output*(1-output)



# sigmoid_test = sigmoid([22,44])

import matplotlib.pyplot as plt 
import numpy as np 
import math 
  
# x = np.linspace(-10, 10, 100)
x =1

x = [-1,0,0.5,1]
# x = [-1.33,0.33,0.533,1.33]
# z = 1/(1 + np.exp(-x)) 

# for val in x:
#     print(val,sigmoid(val))

for val in x:
    print(val,sigmoid(val),sigmoid_output_to_derivative(sigmoid(val)))



# 1 0.7310585786300049
# 0.5 0.6224593312018546
# 0 0.5
# -1 0.2689414213699951

# plt.plot(x, z) 
# plt.xlabel("x") 
# plt.ylabel("Sigmoid(X)") 
  
# plt.show() 