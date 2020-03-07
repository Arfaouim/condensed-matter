from __future__ import print_function
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def D_wrap(A, dX):
	d = A - np.roll(A, 1)
	d = 0.5 * (d + np.roll(d, -1))
	return d

#doesn't wrap over, faster
def D_nowrap(A, dX):
	d = A[1:] - A[:-1]
	d = np.concatenate(([d[0]], d, [d[-1]]))
	d = 0.5 * (d[1:] + d[:-1])
	return d

D = D_nowrap	#select diff function

N = 400		#number of points
size = 10	#x in [-size, size]
dX = 2.*size/N	#x step
dt = 0.0005		#time step

X = np.linspace(-size, size, N)

x0 = -5
A = np.exp(-4*(X-x0)*((X-x0)+1500j))	#initial wave function
A = np.array(A, dtype=np.complex)

#V = np.zeros(N)
V = 0.5*(np.abs(X - 2) < 0.5)		#potential

fig, ax = plt.subplots()
line, = ax.plot(X, A)
ax.set_ylim([0, 1])

ax.plot(X, V)

def animate(i):
	global A

	for i in range(1000):	#don't show every time step
		A += dt*(1j*D(D(A, dX), dX) - 1j * V * A)	#schrodinger equation

	print(np.sum(np.abs(A**2)))	#print norm

	line.set_ydata(np.abs(A**2))

	return line,


ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=True)
plt.show()
