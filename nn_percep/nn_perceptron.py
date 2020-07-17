# https://towardsdatascience.com/6-steps-to-write-any-machine-learning-algorithm-from-scratch-perceptron-case-study-335f638a70f3
# Importing libraries
# NAND Gate
# Note: x0 is a dummy variable for the bias term
#     x0  x1  x2
import numpy as np
x = [[1., 0., 0.],
     [1., 0., 1.],
     [1., 1., 0.],
     [1., 1., 1.]]
y =[1.,
    1.,
    1.,
    0.]
w = np.zeros(len(x[0]))
# Activation Function
z = 0.0
# Dot Product
f = np.dot(w, x[0])
if f > z:
    yhat = 1.
else:
    yhat = 0.
eta = 0.1
w[0] = w[0] + eta*(y[0] - yhat)*x[0][0]
w[1] = w[1] + eta*(y[0] - yhat)*x[0][1]
w[2] = w[2] + eta*(y[0] - yhat)*x[0][2]
print(w[0])
# print(x[0])
# print(y[0])

# print(w[0])
# print(y[0])
# print(x[0][0])
# print(x[0][1])
# print(x[0][2])

# print(len(y))

# print(len(x))

# import numpy as np

# # Perceptron function
# def perceptron(x, y, z, eta, t):
#     '''
#     Input Parameters:
#         x: data set of input features
#         y: actual outputs
#         z: activation function threshold
#         eta: learning rate
#         t: number of iterations
#     '''
    
#     # initializing the weights
#     w = np.zeros(len(x[0]))      
#     n = 0                        
    
#     # initializing additional parameters to compute sum-of-squared errors
#     yhat_vec = np.ones(len(y))     # vector for predictions
#     errors = np.ones(len(y))       # vector for errors (actual - predictions)
#     J = []                         # vector for the SSE cost function
    
#     while n < t: for i in xrange(0, len(x)): # dot product f = np.dot(x[i], w) # activation function if f >= z:                               
#                 yhat = 1.                               
#             else:                                   
#                 yhat = 0.
#             yhat_vec[i] = yhat
            
#             # updating the weights
#             for j in xrange(0, len(w)):             
#                 w[j] = w[j] + eta*(y[i]-yhat)*x[i][j]
                
#         n += 1
#         # computing the sum-of-squared errors
#         for i in xrange(0,len(y)):     
#            errors[i] = (y[i]-yhat_vec[i])**2
#         J.append(0.5*np.sum(errors))
        
#     return w, J