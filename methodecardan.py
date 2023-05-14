# -*- coding: utf-8 -*-
"""
Created on Sun May 14 15:24:54 2023

@author: Nour
"""

import matplotlib.pyplot as py
import numpy as np

###FONCTIONS
def VanderClap(x,Tr):
    return((8*Tr/(3*x-1))-(3/(x**2)))
py.figure(figsize=(8,6), dpi=80)
py.title("Représentation graphique de l'équation de Van Der Waals en coordonnées réduites\n dans le diagramme de Clapeyron")
py.xlabel(r'Vr')
py.ylabel('Pression')
py.grid(alpha=0.3)
py.axis([4e-1,3.5,0.4,1.5])
Z1 = np.arange(0.2,4.5,1e-5)
Z2 = np.arange(0.90,1,0.01)
Z2 = np.append(Z2,1)
Z6,Z7,Z8,Z9 = [],[],[],[]
for u in Z2:
    Z3,Z4,Z5 = [],[],[]
    delta1 = 1
    if u < 1:
        for Pr in np.arange(1,0.1,-1e-5):
            if Pr<1:
                A = 3*Pr
                B = -(Pr+8*u)
                C = 9
                D = -3
                p = C/A - (B**2)/(3*(A**2))
                q = (B/(27*A))*(((2*(B**2))/(A**2))-(9*C)/A)+D/A
                delta = -((q**2)*27 + (p**3)*4)
                if delta > 0:
                    theta = np.arccos(np.radians((3*q)/(2*p)*(np.sqrt(3/-p))))
                    Va = -B/(3*A)+2*np.sqrt(-p/3)*np.cos((1/3)*theta)
                    Vc = -B/(3*A)+2*np.sqrt(-p/3)*np.cos(np.radians((1/3)*theta)+(4*np.pi)/3)
                    PA = VanderClap(Va,u)
                    delta2 = (8/3)*u*np.log(((3*Vc)-1)/((3*Va)-1))+3*((1/Vc)-(1/Va))-PA*(Vc-Va)
                    if abs(delta2)<1e-4 and delta2 <delta1:
                        delta1 = delta2
                        P0 = Pr
    for Vr in Z1:
        Pr = VanderClap(Vr,u)
        Z3.append(Pr)
        if abs(Pr-P0)<1e-5:
            Z4.append(Vr)
            Z5.append(P0)
    if u == 1:
        py.plot(Z1,Z3,label=r'$T_r$= %.2f' %u)
        Z6.append(1)
        Z7.append(1)
        Z8.append(1)
        Z9.append(1)
    else:
        L1c = Z1.tolist()
        lsat = min(Z4)
        gsat = max(Z4)
        x = L1c.index(lsat)
        y = L1c.index(gsat)
        Z6.append(lsat)
        Z7.append(VanderClap(lsat,u))
        Z8.append(gsat)
        Z9.append(VanderClap(gsat,u))
        py.plot(L1c[:x]+L1c[y:],Z3[:x]+Z3[y:],label=r'$T_r$= %.2f' %u)
        py.plot(Z4,Z5,color='purple',label=r'$P_0$=%.3f' %(sum(Z5)/len(Z5)))
py.plot(Z6,Z7,label = 'Courbe ebullition', color='red',linewidth=1.5)
py.plot(Z8,Z9,label='Courbe de rosée', color='darkblue',linewidth=1.5)
py.legend(loc='upper right')
py.show()