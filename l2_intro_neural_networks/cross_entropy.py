import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    centropy = 0
    for i, yi in enumerate(Y):
        centropy += -1 * (yi* np.log(P[i]) + (1-yi)*np.log(1-P[i]))
    return centropy 
    
Y = [1,1,0]
P = [0.8,0.7,0.1]

print(cross_entropy(Y,P))

Y = [1,0,1,1]
P = [0.4,0.6,0.1,0.5]

cp = cross_entropy(Y,P)
print(cp)
assert cp == 4.828313737302301