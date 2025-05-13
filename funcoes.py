from parametros import *
from math import *

def modelo(lista,t):
    y=lista[0]
    vy=lista[1]
    dydt=vy
    p = p0*(e**(-y/h0))
    if y>= 2455: 
        A = 0.75     #Área de uma pessoa com os braços abertos
        Cd= 1.3      #Coeficiente de arrasto do ar para uma pessoa em queda livre
    else:            #Após a abertura do paraquedas
        A = 20       #Área do paraquedas aberto 
        Cd= 2        #Coeficiente de arrasto do ar para o paraquedas
    dvydt = ((p*Cd*A*(vy)**2)/2*mt) - (G*M/((R+y)**2))
    return [dydt,dvydt]