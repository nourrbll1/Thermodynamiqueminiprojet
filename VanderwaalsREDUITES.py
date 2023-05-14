# -*- coding: utf-8 -*-
"""
Created on Sun May 14 14:43:38 2023

@author: Nour
"""

import matplotlib.pyplot as py
import numpy as np

###CONSTANTES
R1=0.0820574587
R2=8.314
Tgp=500
Tgp1=1000
Tgp2=3000
Tgp3=6000
Tgp4=9000
avw=1
bvw=4
Tvw1=100
Tvw2=200
Tvw3=300
P1,P2,P3,P4,P5,P6 = [],[],[],[],[],[]
F1,F2,F3,F4,F5,F6 = [],[],[],[],[],[]
E1,E2,E3,E4,E5,E6 = [],[],[],[],[],[]
S1,S2,S3,S4,S5,S6 = [],[],[],[],[],[]
X1,X2,X3,X4,X5,X6 = [],[],[],[],[],[]
P1,P2,P3,P4,P5,P6 = [],[],[],[],[],[]
L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12 = [],[],[],[],[],[],[],[],[],[],[],[]
Tr=[1.03,1.02,1.01,1,0.99,0.98,0.97]
aclap = 363.7*(10**-3)
bclap=0.0427*(10**-3)
###FONCTION
def VanderClap(x,Tr):
    return((8*Tr/(3*x-1))-(3/(x**2)))
py.figure(figsize=(8,6), dpi=80)
py.title("Représentation graphique de l'équation de Van der Waals en coordonnées de Clapeyron")
ax = py.gca()
ax.set_xlabel('Vr',labelpad = 10)
ax.set_ylabel('Pr',labelpad = 1)
ax.grid(True)
X=np.linspace(0.4,2,256,endpoint=True)
py.xlim(0.4,2)
py.ylim(0.8,1.4)
Y=[]
for t in range (0,len(Tr)):
    y=VanderClap(X,Tr[t])
    Y.append(y)
py.plot( X,Y[0], color="blue", linewidth=1.0, linestyle="-",label="Tr=1.03")
py.plot( X,Y[1], color="blue", linewidth=1.0, linestyle="-",label="Tr=1.02")
py.plot( X,Y[2], color="blue", linewidth=1.0, linestyle="-",label="Tr=1.01")
py.plot( X,Y[3], color="red", linewidth=1.5, linestyle="-",label="Tr=1.00 isotherme point critique ")
py.plot( X,Y[4], color="blue", linewidth=1.0, linestyle="-",label="Tr=0.99")
py.plot( X,Y[5], color="blue", linewidth=1.0, linestyle="-",label="Tr=0.98")
py.plot( X,Y[6], color="blue", linewidth=1.0, linestyle="-",label="Tr=0.97")
py.scatter([1,],[1,], 200, color ='red')
#py.annotate('Point Critique', xy=(1, 1), xytext=(1.4,1.15), arrowprops=dict(arrowstyle="->"))
py.legend(loc='upper right')
py.show()