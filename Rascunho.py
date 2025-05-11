mt = 150                #Massa do conjunto humano + acessorios
M =  5.972*1e24          #Massa da Terra
G = 6.67*1e-11           #Constante de gravitação universal
R = 6371000             #Raio da Terra
po = 1.225              #PEDIR NOME
ho = 7500               #PEDIR NOME

import pandas
from math import*
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def modelo(Y, t):
    y =Y[0]
    vy = Y[1]
    if y>= 2455: 
        A = 0.75     #Área de uma pessoa com os braços abertos
        Cd= 1.3      #Coeficiente de arrasto do ar para uma pessoa em queda livre
    else:            #Após a abertura do paraquedas
        A = 20       #Área do paraquedas aberto 
        Cd= 2        #Coeficiente de arrasto do ar para o paraquedas
    p = po*(e**(-y/ho))
    dydt = vy
    dvydt = (p*Cd*A*(vy)**2)/2*mt - (G*M/((R+y)**2))
    L = [dydt, dvydt]
    return L

y0 = 38969           #Altura inicial do humano (m)
v0 = 1.94            #Velocidade inicial (m/s)
Y0 = [y0, v0]        # Condicoes iniciais

dt = 0.001
tf = 9*60 + 7 
lista_t = np.arange(0, tf, dt)

q = odeint(modelo, Y0, lista_t)
y_lista = q[:,0]
vy_lista = abs(q[:,1])

plt.plot(lista_t/60, y_lista)
plt.title("Altura x Tempo")
plt.xlabel("Tempo (minutos)")
plt.ylabel("Altura (metros) ")
plt.grid()
plt.show()

plt.plot(lista_t/60, vy_lista)
plt.title("Velocidade x Tempo")
plt.xlabel("Tempo (minutos)")
plt.ylabel("Velocidade (m/s)")
plt.grid()
plt.show()