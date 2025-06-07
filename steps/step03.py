
import numpy as np
from steps.step01 import Variable
from steps.step02 import Exp, Square


A = Square()
B = Exp()
C = Square()

x = Variable(np.array(0.5))
a = A(x)
b = B(a)
y = C(b)
print(y.data)