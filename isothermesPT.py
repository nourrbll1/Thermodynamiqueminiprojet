# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:41:56 2023

@author: Nour
"""

import matplotlib.pyplot as py
import numpy as np

def EquationGazParfait(V,T,R):
    return((R*T)/V)

def Vander(x,a,b,k):
    return((k/(x-b))-(a/(x**2)))

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
py.figure(figsize = (10,6), dpi=80)
ax = py.gca()
py.title("Représentation graphique de la pression en fonction de la température pour le CO₂ en tant que gaz parfait et de Van Der Waals")
ax.set_xlabel('Température',labelpad = 10)
ax.set_ylabel('Pression',labelpad = 10)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
py.grid(True)
py.xlim(0,1500)
py.ylim(0,40000000)
V = [p/100000 for p in range (1,111,20)]
T = [t for t in range(300,1301)]
for j in range (len(T)):
    e1 = EquationGazParfait(0.00001,T[j],R2)
    E1.append(e1)
    e2 = EquationGazParfait(V[1],T[j],R2)
    E2.append(e2)
    e3 = EquationGazParfait(V[2],T[j],R2)
    E3.append(e3)
    e4 = EquationGazParfait(V[3],T[j],R2)
    E4.append(e4)
    e5 = EquationGazParfait(V[4],T[j],R2)
    E5.append(e5)
    e6 = EquationGazParfait(V[5],T[j],R2)
    E6.append(e6)
for j in range (len(T)):
    s1 = Vander(V[0],aclap,bclap,T[j]*R2)
    S1.append(s1)
    s2 = Vander(V[1],aclap,bclap,T[j]*R2)
    S2.append(s2)
    s3 = Vander(V[2],aclap,bclap,T[j]*R2)
    S3.append(s3)
    s4 = Vander(V[3],aclap,bclap,T[j]*R2)
    S4.append(s4)
    s5 = Vander(V[4],aclap,bclap,T[j]*R2)
    S5.append(s5)
    s6 = Vander(V[5],aclap,bclap,T[j]*R2)
    S6.append(s6)
py.plot(T,E1,color="purple",linewidth=1.5, linestyle="-",label='Gaz parfait')
py.plot(T,E2,color="purple",linewidth=1.5, linestyle="-")
py.plot(T,E3,color="purple",linewidth=1.5, linestyle="-")
py.plot(T,E4,color="purple",linewidth=1.5, linestyle="-")
py.plot(T,E5,color="purple",linewidth=1.5, linestyle="-")
py.plot(T,E6,color="purple",linewidth=1.5, linestyle="-")
py.plot(T,S1,color="green",linewidth=1.5, linestyle="-",label='Van Der Waals')
py.plot(T,S2,color="green",linewidth=1.5, linestyle="-")
py.plot(T,S3,color="green",linewidth=1.5, linestyle="-")
py.plot(T,S4,color="green",linewidth=1.5, linestyle="-")
py.plot(T,S5,color="green",linewidth=1.5, linestyle="-")
py.plot(T,S6,color="green",linewidth=1.5, linestyle="-")
py.legend(loc='upper right')
py.show()