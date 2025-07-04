# steps/step04
# 导数, 复合函数的导数

import numpy as np
from steps.step01 import Variable
from steps.step02 import Exp, Square


def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(x.data - eps)
    x1 = Variable(x.data + eps)
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2 * eps)

def f(x):
    A = Square()
    B = Exp()
    C = Square()
    return C(B(A(x)))

f1 = Square()
x = Variable(np.array(2.0))
dy = numerical_diff(f1, x)

x = Variable(np.array(0.5))
# 函数也可以作为参数传给其他函数
dy = numerical_diff(f, x)

print(dy)