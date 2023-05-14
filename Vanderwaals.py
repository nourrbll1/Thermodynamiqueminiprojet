# -*- coding: utf-8 -*-
"""
Created on Sat May 13 21:41:23 2023

@author: Nour
"""

import matplotlib.pyplot as py
import numpy as np


R1=0.0820574587
R2=8.314
Tgp=500
Tgp1=1000
Tgp2=3000
Tgp3=6000
Tgp4=9000
avw=1
bvw=4
Tvw1=10
Tvw2=20
Tvw3=30
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


def Vander(x,a,b,k):
    return((k/(x-b))-(a/(x**2)))

py.figure(figsize=(8,6), dpi=80)
py.title("Représentation graphique de l'équation de Van der Waals")
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
py.xlim(-7.5,7.5)
py.ylim(-400,400)
X = np.linspace(-7.5, 7.5, 256,endpoint=True)
Y = np.linspace(-400,400, 256,endpoint=True)
X = np.linspace(-15, 15, 256,endpoint=True)
W1=Vander(X,avw,bvw,Tvw1)
W2=Vander(X,avw,bvw,Tvw2)
W3=Vander(X,avw,bvw,Tvw3)
py.plot( X,Y, color="none",label="a=1 et b=4")
py.plot( X,W1, color="black", linewidth=1.0, linestyle="-",label="T=10 K,")
py.plot( X,W2, color="blue", linewidth=1.0, linestyle="-",label="T=20 K")
py.plot( X,W3, color="red", linewidth=1.0, linestyle="-",label="T=30 K")
py.axvspan(-10,0,facecolor='yellow', alpha=0.3, label='Partie Non Réelle')
py.axvspan(0,10,ymax=0.5,facecolor='yellow', alpha=0.3)
py.legend(loc='upper left')
py.show()