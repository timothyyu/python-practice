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
# z = 1/(1 + np.exp(-x)) 
for val in x:
    print(val,sigmoid(val))

# plt.plot(x, z) 
# plt.xlabel("x") 
# plt.ylabel("Sigmoid(X)") 
  
# plt.show() 