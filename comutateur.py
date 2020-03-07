from sympy.physics.quantum import Commutator, Dagger, Operator
from sympy.abc import x, y


A = Operator('A')
B = Operator('B')
C = Operator('C')
comm = Commutator(A, B)

#[A,B]
comm.doit()
#A*B - B*A
comm = Commutator(B, A); comm
#-[A,B]
Commutator(3*x*A, x*y*B)
#3*x**2*y*[A,B]
Commutator(A+B, C).expand(commutator=True)
#[A,C] + [B,C]
Commutator(A, B+C).expand(commutator=True)
#[A,B] + [A,C]
Commutator(A*B, C).expand(commutator=True)
#[A,C]*B + A*[B,C]
Commutator(A, B*C).expand(commutator=True)
#[A,B]*C + B*[A,C]
Dagger(Commutator(A, B))
#-[Dagger(A),Dagger(B)]
