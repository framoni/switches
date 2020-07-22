import numpy as np
from sympy import *

x1, x2, x3, x4 = symbols('x:4')

res = solve([cos(pi*(x1+x2+x3))+1,
             cos(pi*(x1+x2+x4))-1,
             cos(pi*(x1+x3+x4))-1,
             cos(pi*(x2+x3+x4))-1],
            [x1, x2, x3, x4])

np.array(res)

# turns out sympy doesn't provide all solutions for nonlinear systems with trigonometric functions
