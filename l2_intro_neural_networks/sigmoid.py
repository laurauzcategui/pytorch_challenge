import math 

def sigmoid(x):
    return 1 / ( 1 + math.exp(-x))

def perceptron():
    x = [(1,1), (2,4), (5,-5), (-4,5)]

    for xi in x: 
        score = 4 * xi[0] + 5 * xi[1] -9 
        sig = sigmoid(score)
        print("X:{} Score:{} Sigmoid:{}".format(xi, score, sig))

perceptron()