from sympy import symbols
from sympy.physics.quantum import AntiCommutator
from sympy.physics.quantum import Operator, Dagger
x, y = symbols('x,y')
A = Operator('A')
B = Operator('B')
        
ac = AntiCommutator(A,B); ac
print(ac)

#doit multiple the anti A*B + B*A
ac.doit()
#define un autre anti 
ab=AntiCommutator(3*x*A,x*y*B)
#Adjoint operations applied to the anticommutator are properly applied to the arguments:
aa=Dagger(AntiCommutator(A,B))
