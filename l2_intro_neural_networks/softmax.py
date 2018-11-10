import numpy as np

# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax(L):
    softmax_values = []
    for e in L:
        softmax_values.append(np.exp(e) / np.sum(np.exp(L)))
    return softmax_values

L=[5,6,7]
print(softmax(L))