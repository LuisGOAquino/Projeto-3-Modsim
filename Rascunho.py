mt = 150                #Massa do conjunto humano + acessorios
M =  5.972e24          #Massa da Terra
G = 6.67e-11           #Constante de gravitação universal
R = 6371000             #Raio da Terra
po = 1.225              #Densidade ao nível do mar
ho = 7500               #Constante de decaimento exponencial

import pandas
from math import*
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def modelo(Y, t):
    y = Y[0]
    vy = Y[1]
    if y >= 2560: 
        A = 1.0     #Área de uma pessoa com os braços abertos
        Cd= 1.1      #Coeficiente de arrasto do ar para uma pessoa em queda livre
    else:            #Após a abertura do paraquedas
        A = 20       #Área do paraquedas aberto 
        Cd= 2        #Coeficiente de arrasto do ar para o paraquedas
    p = po*(e**(-y/ho))
    dydt = vy
    dvydt = (p*Cd*A*(vy**2))/(2*mt) - (G*M/((R+y)**2))
    L = [dydt, dvydt]
    return L

y0 = 38969           #Altura inicial do humano (m)
v0 = 0            #Velocidade inicial (m/s)
Y0 = [y0, v0]        # Condicoes iniciais

dt = 1
tf = 400
lista_t = np.arange(0, tf, dt)

q = odeint(modelo, Y0, lista_t)
y_lista = q[:,0]
vy_lista = abs(q[:,1])

# print (y_lista)
# print (vy_lista)
plt.plot(lista_t, y_lista)
plt.title("Altura x Tempo")
plt.xlabel("Tempo (segundos)")
plt.ylabel("Altura (metros) ")
plt.grid()
plt.show()

plt.plot(lista_t, vy_lista)
plt.title("Velocidade x Tempo")
plt.xlabel("Tempo (segundos)")
plt.ylabel("Velocidade (m/s)")
plt.grid()
plt.show()


# po = 1.225              #PEDIR NOME
# ho = 7500               #PEDIR NOME
# p = po*(e**(-y/ho))

# a = np.arange(38969, 0, -10)

# for al in a:

# def densi(ly):
#     r = []
#     for al in ly:
#         p = po*(e**(-al/ho))


