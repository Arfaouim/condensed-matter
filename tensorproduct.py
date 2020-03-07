from __future__ import division
from sympy import *
from sympy.physics.quantum import Dagger
x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

from sympy import I, Matrix, symbols
from sympy.physics.quantum import TensorProduct
m1 = Matrix([[1,2],[3,4]])
m2 = Matrix([[1,0],[0,1]])
TensorProduct(m1, m2)


A=Symbol('A',commutative=False)
B=Symbol('B',commutative=False)
C = Symbol('C',commutative=False)
D = Symbol('D',commutative=False)


tp=TensorProduct(A,B)#A⊗B



Dagger(tp)#adjoint
#Dagger(A)xDagger(B)

l = TensorProduct(A+B,C)
#(A + B)xC
l.expand(tensorproduct=True)
#AxC + BxC
e = TensorProduct(A,B)*TensorProduct(C,D)
#AxB*CxD
tensor_product_simp(e)
#(A*C)x(B*D)
