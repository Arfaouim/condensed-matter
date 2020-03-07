import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
mu = 0.55 #ev
k = 8.6e-5 #Valeur en eV/K

#variation de T k
T_min = 0   # the minimial value of the paramater a
T_max =30000   # the maximal value of the paramater a
Ti = 300  # the value of the parameter a to be used initially, when the graph is created


def f(e):
     return 1.0 / (np.exp((e - mu)/(k*Ti)) + 1)
fig = plt.figure()
espan = np.linspace(-0.5, 3, 200)

# plt.axes((left, bottom, width, height), facecolor='w')
sin_ax = plt.axes([0.15, 0.2, 1, 0.65])
plt.axes(sin_ax)
plt.suptitle('Fermi-Dirac distribution function')
plt.title('f(E)= E')
plt.xlabel('E')
plt.ylabel('f(E)',rotation=0)
fd,=plt.plot(espan, f(espan),'r')
plt.xlim(-0.5, 1.5)

plt.ylim(0, 1.1)


plt.text(0.75,0.8, 'Destrubition\nFermi_Dirac', style='italic',
     bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})


# here we create the slider
t_slider = Slider(plt.axes([0.2, 0.05, 0.65, 0.05])
          ,      # the axes object containing the slider
      'Varie T(K)',            # the name of the slider parameter
      T_min,          # minimal value of the parameter
      T_max,          # maximal value of the parameter
      valinit=Ti  # initial value of the parameter
     )
def update(T):
    fd.set_ydata( 1.0 / (np.exp((espan - mu)/(k*t_slider.val)) + 1)) 
    fig.canvas.draw_idle()


t_slider.on_changed(update)

plt.show()
