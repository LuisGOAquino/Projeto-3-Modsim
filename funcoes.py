from parametros import *
import pandas
from math import *
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