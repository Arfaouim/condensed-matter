"""
Martouzet Grégoire - gregoire.martouzet@ens-paris-saclay.fr

----------------------------------------

"Tout" ce qu'il faut pour le ferromagnétisme:
 - résolution de l'équation auto-cohérente en champ moyen pour différentes températures et différents champs magnétiques
 - affichage de l'énergie libre dans le cas du model de Landau (pour différentes températures)
 
Pour modifier le comportement du programme: completer la variable "Sortie"
 
Equation auto-cohérente (cf DIU - Physique statistique):
tanh(x) = T/Tc*x - B/B0

  avec:
	x = M/M_inf
	M_inf = N*g*nu_b/(2*V)
	Tc = température critique
	B0 = -g*mu_b/(2*k*Tc)

Energie libre de Landau:
F = alpha*(T/Tc-1)*m**2 + beta*m**4
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider


# Sortie:
# 1 - Graphique avec slider sur B
# 2 - plusieurs champs B sur le même graphique
# 3 - Résolution graphique de l'équation (avec Slider)
# 4 - Modèle de Landau
Sortie = 3


""" ----- Paramètres ----- """
N = 1000 # Nombre de point à calculer

temperature = np.linspace(0.25,1.75, 100)

x = np.linspace(-20, 20, N)

# Champ magnétique pour sortie 2
chp_b = [0, 1e-3, 0.01, 0.08]

# liste de température pour Landau
liste_t_landau = [0.001,0.01,0.1,1,10]

# Aimantation pour Landau
m_landau = np.linspace(-10,10,N)



""" ---------- """



# Fonction pour le champ moyen
def fct1(x):
	return np.tanh(x)
	
def fct2(x, t, b):
	return t*x - b

# Fonction cohérente par défaut
y1= fct1(x)

# Energie libre de Landau
def F(m, T):
	
	alpha = 1
	beta = 1e-2
	Tc = 1
	
	return alpha*(T/Tc-1)*m**2 + beta*m**4

# recherche des solutions de l'équation auto-cohérente
def search_and_append(y1, y2, t, T, M, X):
	y = y1-y2
	
	y3 = np.roll(y, 1)
	y3[0] = y[0]
	
	y3 *= y
	
	for i in range(len(y2)-1):
		if y3[i]<0:
			A = abs(y[i-1]/y[i])
			x_p = (A*x[i]+x[i-1])/(1+A)
			
			M.append( fct1(x_p) )
			T.append( t )
			X.append( x_p )
	
""" ----- fonctions de mise à jour des graphiques (uniquement dans le cas de champ moyen)----- """		

# MAJ lors d'une modification de B
def update(B):
	T, M = [], []
	
	# pour chaque température, on cherche les solutions
	for t in temperature:
		y2 = fct2(x, t, B)
		search_and_append(y1, y2, t, T, M, [])
	
	return T, M

# MAJ lors d'une modification de B
def update_graph(val):
	T, M = update(val)
	l.set_data(T, M)
	fig.canvas.draw_idle()
	
# MAJ lors d'une modification de B ou T (pour la sortie 3)
def update_graph_sortie3(val):
	param_t = sT.val
	param_B = sB.val
	
	# détermination de la nouvelle fonction auto-cohérente
	y2 = fct2(x, param_t, param_B)
	
	l.set_ydata( y2 )
	
	T = []
	M = []
	X = []
	
	# recherche des solutions
	search_and_append(y1, y2, param_t, T, M, X)
	
	l2.set_data(X, M)
	
	fig.canvas.draw_idle()
	
	
""" Affichage différent selon la sortie choisie """

if Sortie == 1:
	# 1 - Graphique avec slider sur B
	
	# création axe
	fig, ax = plt.subplots()
	plt.subplots_adjust(bottom=0.25)

	# recherche de solution pour B=0.0
	T, M = update(0.0)

	l, = plt.plot(T, M, '.')
	
	plt.ylim(-1.2,1.2)
	plt.xlabel("$T/T_c$")
	plt.ylabel("$M/M_\infty$")
	
	# Création slider sur B
	axB = plt.axes([0.1, 0.1, 0.65, 0.03])
	sB = Slider(axB, '$B/B_0$', 0, 0.05, valinit=0.0)
	sB.on_changed(update_graph)
	
elif Sortie == 2:
	# 2 - plusieurs champs B sur le même graphique

	# recherche de solution pour différent B fixé
	line = []
	for b in chp_b:
		T, M = update(b)

		l, = plt.plot(T, M, '.')
		line.append(l)
		
	plt.ylim(-1.2,1.2)
	plt.xlabel("$T/T_c$")
	plt.ylabel("$M/M_\infty$")

	plt.legend(line, ["$B/B_0$ = "+str(b) for b in chp_b])
	
elif Sortie == 3:
	# 3 - Résolution graphique de l'équation (avec Slider)

	fig, ax = plt.subplots()
	plt.subplots_adjust(bottom=0.3)
	
	plt.axis([-7.5,7.5,-1.2,1.2])
	
	y1 = fct1(x)
	y2 = fct2(x, 0.5, 0.0)
	
	# Tracer des deux fonctions à égaliser
	plt.plot(x, y1)
	l, = plt.plot(x, y2)
	
	# Recherche de solutions
	T = []
	M = []
	X = []
	search_and_append(y1, y2, 0.5, T, M, X)
	
	# Petit ronds rouges au niveau des solutions
	l2, = plt.plot(X, M, 'or')
	
	# Slider pour T et B
	axT = plt.axes([0.1, 0.2, 0.65, 0.03])
	sT = Slider(axT, '$T/T_c$', 0.25, 1.5, valinit=0.5)
	sT.on_changed(update_graph_sortie3)
	
	axB = plt.axes([0.1, 0.1, 0.65, 0.03])
	sB = Slider(axB, '$B/B_0$', 0, 0.05, valinit=0)
	sB.on_changed(update_graph_sortie3)
elif Sortie == 4:
	# 4 - Modèle de Landau
	
	
	# Calcul de F en fonction de l'aimantation pour chaque température
	for T in liste_t_landau:
		f = F(m_landau, T)
		plt.plot(m_landau, f, label='$T=$'+str(T))
				
	plt.axis([-10,10,-30,100])
	plt.legend()
else:
	print("Variable 'Sortie' non valide: 1, 2, 3 ou 4")
	# La variable Sortie n'est pas valide, il faut vérifier sa valeur en début de code

plt.show()
