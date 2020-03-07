'''
Ce programme trace l'allure (en unités arbitraires) de la composante
normale du champ électrique à l'interface vide-conducteur, dans le régime
des fréquences décrit par l'équation de Klein-Gordon, à une pulsation
inférieure à la pulsation plasma.
'''

from pylab import *
from matplotlib import animation

dt = 0.01
w=2*pi
k=2*pi
kk=0.3*pi
delta=1

zed=linspace(0,10,1000)
zedneg=linspace(-5,0,500)

fig=figure()

subplot()

title(r"Cas : $\omega<\omega_p$")
xlabel('$z$')
ylabel(r'$E_x/E_0$')
ylim([-1.5,1.5])
xlim([-5,10])
E=[exp(-kk*z) for z in zed]
line1,=plot([],[],color='r')
line2,=plot([],[],color='r')
line3,=plot(zedneg,[cos(-k*z) for z in zedneg],ls='dashed',color='g')
line4,=plot(zedneg,[sin(-k*z) for z in zedneg],ls='dashed',color='b')

# fonction à définir quand blit=True
# crée l'arrière de l'animation qui sera présent sur chaque image
def init():
    line1.set_data([],[])
    line2.set_data([],[])
    line3.set_data([],[])
    line4.set_data([],[])
    #matplotlib.pyplot.xticks( [0, 2, 4, 6, 8, 10],
    #        [r'0',r'$2\delta$',r'$4\delta$',r'$6\delta$',r'$8\delta$',r'$10\delta$'])
    plt.plot([0,0],[-2,2],color='k')
    return line1,line2,line3,line4,

def animate(i): 
    t = i * dt
    Ei=[0.5*cos(w*t-k*z) for z in zedneg]
    Er=[0.5*cos(w*t+k*z) for z in zedneg]
    Es=[Ei[i]+Er[i] for i in range(500)]
    Et=[Es[499]*exp(-kk*z) for z in zed]
    line1.set_data(zed,Et)
    line2.set_data(zedneg,Es)
    line3.set_data(zedneg,Ei)
    line4.set_data(zedneg,Er)
    return line1,line2,line3,line4,
 
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=2000, blit=True, interval=20, repeat=False)

subplot()

show()
