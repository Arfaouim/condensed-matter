import numpy
import math
import cmath


class Schrodinger1D:
    def __init__(self,L,N):
        self.L = L
        self.N = N
        self.dx = L/(N-1)
        self.b = numpy.zeros(N,dtype=numpy.complex)
        self.e = numpy.zeros(N,dtype=numpy.complex)
        self.x = numpy.zeros(N,dtype=numpy.complex)
        self.beta = numpy.zeros(N,dtype=numpy.complex)
        self.gamma = numpy.zeros(N,dtype=numpy.complex)
        
    def config(self,dt,V):
        N = self.N
        self.dt = dt
        dx2 = self.dx*self.dx
        alpha = 2*dx2/dt
        for k in range(1,self.N-1):
            self.b[k] = 1j*alpha-dx2*V[k]-2.0
            self.e[k] = 1j*alpha+dx2*V[k]+2.0
        self.b[0] = 1.0
        self.b[N-1] = 1.0
        self.beta[0] = self.b[0]
        self.gamma[0] = 1.0/self.beta[0]
        for k in range(1,N):
            self.beta[k] = self.b[k]-self.gamma[k-1]
            if self.beta[k]==0:
                raise Exception("Impossible de resoudre le systeme ligne "+str(k))
            self.gamma[k] = 1.0/self.beta[k]
            
    def iterations(self,psi0,ti,tf):
        if psi0.size!=self.N:
            raise Exception("Taille de U incorrecte")
        psi = psi0.copy()
        t = ti
        while t<tf:
            self.x[0] = (self.e[0]*psi[0]-psi[1])/self.beta[0]
            for k in range(1,self.N-1):
                self.x[k] = (-psi[k-1]+self.e[k]*psi[k]-psi[k+1]-self.x[k-1])/self.beta[k]
            k = self.N-1
            self.x[k] = (-psi[k-1]+self.e[k]*psi[k]-self.x[k-1])/self.beta[k]
            psi[self.N-1] = self.x[self.N-1]
            for k in range(self.N-2,-1,-1):
                psi[k] = self.x[k]-self.gamma[k]*psi[k+1]
            t += self.dt
        return [psi,t]
            
    def V_marche(self,V0):
        V = numpy.zeros(self.N)
        P = int(self.N/2)
        V[P:self.N-1] = V0
        return V
        
    def V_barriere(self,V0,largeur):
        q = int(largeur/self.dx/2)
        V = numpy.zeros(self.N)
        P = int(self.N/2)
        V[P-q:P+q] = V0
        return V
     
    def paquet(self,x0,k0,sigma0):
        psi = numpy.zeros(self.N,dtype=numpy.complex)
        for k in range(1,self.N-1):
            x = self.dx*k
            psi[k] = cmath.exp(1j*k0*x)*math.exp(-(x-x0)*(x-x0)/(4*sigma0**2))
        return psi




    
            
