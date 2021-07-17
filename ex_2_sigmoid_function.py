import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    nom = sum(np.exp(L))
    
    output = []
    for i in L:
        output.append(np.exp(i)/nom)
        
    return output