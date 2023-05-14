# -*- coding: utf-8 -*-
"""
Created on Sat May 13 19:58:23 2023

@author: Nour
"""

import matplotlib.pyplot as py
import numpy as np


def EquationGazParfait(V,T,R):
    return((R*T)/V)


R1=0.0820574587
R2=8.314
Tgp1=1500
Tgp2=3000
Tgp3=4500
Tgp4=6000
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
py.figure(figsize=(8,6), dpi=80)
py.title("Représentation graphique mathématiques de l'équation des gaz parfaits")
ax = py.gca()
ax.set_xlabel('Volume molaire',loc='right')
ax.set_ylabel('Pression',loc='top')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
ax.grid(True)
py.xlim(-10,10)
py.ylim(-2000,2000)
X = np.linspace(-10, 10, 256,endpoint=True)
Y = np.linspace(-2000,2000, 256,endpoint=True)
Ev1=EquationGazParfait(X,Tgp1,R1)
Ev2=EquationGazParfait(X,Tgp2,R1)
Ev3=EquationGazParfait(X,Tgp3,R1)
Ev4=EquationGazParfait(X,Tgp4,R1)
py.plot( X,Ev1, color="blue", linewidth=1.5, linestyle="-",label="T=1500 K")
py.plot( X,Ev2, color="black", linewidth=1.5, linestyle="-",label="T=3000 K")
py.plot( X,Ev3, color="red", linewidth=1.5, linestyle="-",label="T=4500 K")
py.plot( X,Ev4, color="green", linewidth=1.5, linestyle="-",label="T=6000 K")
py.axvspan(-10,0,facecolor='grey', alpha=0.3, label='Partie Impossiblephysiquement')
py.axvspan(0,10,ymax=0.5,facecolor='grey', alpha=0.3)
py.legend(loc='upper right')
py.show()
