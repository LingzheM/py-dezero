# steps/step01

import numpy as np

class Variable:
    def __init__(self, data):
        self.data = data

class Function:
    def __call__(self, input):
        x = input.data
        y = x ** 2
        output = Variable(y)
        return output

x = Variable(data=np.array(10))
f = Function()

#print(type(f(x)))
#print(f(x).data)