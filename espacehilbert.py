from sympy import symbols,Interval, oo
from sympy.physics.quantum.hilbert import ComplexSpace,L2
c1 = ComplexSpace(2)
#C(2)
c1.dimension
#2

n = symbols('n')
c2 = ComplexSpace(n)
#C(n)
c2.dimension
#n
hs = L2(Interval(0,oo))
#L2(Interval(0, oo))
hs.dimension
#oo
hs.interval
#Interval(0, oo)
