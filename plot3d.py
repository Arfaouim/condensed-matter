from sympy import symbols, cos
from sympy.plotting import plot3d
x,y = symbols('x y')
plot3d(x*y, (x, -1, 1), (y, -1, 1))
