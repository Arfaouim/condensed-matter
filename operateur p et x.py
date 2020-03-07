from sympy.physics.quantum.cartesian import XOp, XKet, PxOp, PxKet
from sympy.physics.quantum.operatorset import operators_to_state
from sympy.physics.quantum.represent import rep_expectation
from sympy.physics.quantum.operator import Operator
operators_to_state(XOp)
#|x>
operators_to_state(XOp())
#|x>
operators_to_state(PxOp)
#|px>
operators_to_state(PxOp())
#|px>
operators_to_state(Operator)
#|psi>
operators_to_state(Operator())
#|psi>

rep_expectation(XOp())
#x_1*DiracDelta(x_1 - x_2)
rep_expectation(XOp(), basis=PxOp())
#<px_2|*X*|px_1>
rep_expectation(XOp(), basis=PxKet())
#<px_2|*X*|px_1>
