from sympy.vector import CoordSys3D,Del,curl, divergence,gradient, directional_derivative



c=CoordSys3D('c')

nabla=Del()
gradient_field=nabla(c.x*c.y*c.z)

gradient_field.doit()
#C.y*C.z*C.i + C.x*C.z*C.j + C.x*C.y*C.k



#rotatation

    #1ers methode
nabla.cross(c.x*c.y*c.z*c.i).doit()
(nabla ^ c.x*c.y*c.z*c.i).doit()

    #2eme methode
curl(C.x*C.y*C.z*C.i)
#C.x*C.y*C.j + (-C.x*C.z)*C.k


#divergence

  #1ere methode
nabla.dot(c.x*c.y*c.z*(c.i + c.j + c.k)).doit()
#C.x*C.y + C.x*C.z + C.y*C.z
(nabla & c.x*c.y*c.z*(c.i + c.j + c.k)).doit()
#C.x*C.y + C.x*C.z + C.y*C.z
  #2eme methode:
divergence(c.x*c.y*c.z*(c.i + c.j + c.k))
#c.x*C.y + C.x*C.z + C.y*C.z



#Gradient
    #1ere methode
""""Consider a scalar field f(x,y,z) in 3D space. The gradient of this field is defined as the vector of the 3 partial derivatives of f with respect to x, y and z in the X, Y and Z axes respectively.

In the 3D Cartesian system, the divergence of a scalar field f, denoted by ∇f is given by -

∇f=∂f∂xi^+∂f∂yj^+∂f∂zk^

Computing the divergence of a vector field in sympy.vector can be accomplished in two ways.

One, by using the Del() class"""
gradient(c.x*c.y*c.z)
#c.y*c.z*c.i+c.x*c.z*c.j+c.x*x.y*c.k.

#or
nabla.gradient(c.x*c.y*c.z).doit()
#C.y*C.z*C.i + C.x*C.z*C.j + C.x*C.y*C.k
nabla(c.x*c.y*c.z).doit()
#C.y*C.z*C.i + C.x*C.z*C.j + C.x*C.y*C.k



