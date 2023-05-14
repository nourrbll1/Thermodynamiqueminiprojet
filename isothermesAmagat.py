# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:46:40 2023

@author: Nour
"""

import matplotlib.pyplot as py
import numpy as np

def EquationGazParfait(V,T,R):
    return((R*T)/V)

def Vander(x,a,b,k):
    return((k/(x-b))-(a/(x**2)))


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
py.figure(figsize=(10,6), dpi=80)
ax = py.gca()
py.title ("Représentation graphique du réseaux d'isothermes du CO₂ dans le diagramme d'Amagat")
ax.set_xlabel('Pression',labelpad = 10)
ax.set_ylabel( 'PV',labelpad = 10)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
py.grid(True)
py.xlim(0,2.5*10**7)
py.ylim(0,9000)
V=np.arange(0.05e-3,1e-3,1e-5)
T=np.arange(300,1301,200)
xval=[]
yval=[]
for y in range(0,8517):
    o =(-aclap*y+bclap*y**2)/(-2*aclap*bclap)
    xval.append(o)
    yval.append(y)
for j in range (len(V)):
    x1 = EquationGazParfait(V[j],T[0],R2)
    X1.append(x1)
    x2 = EquationGazParfait(V[j],T[1],R2)
    X2.append(x2)
    x3 = EquationGazParfait(V[j],T[2],R2)
    X3.append(x3)
    x4 = EquationGazParfait(V[j],T[3],R2)
    X4.append(x4)
    x5 = EquationGazParfait(V[j],T[4],R2)
    X5.append(x5)
    x6 = EquationGazParfait(V[j],T[5],R2)
    X6.append(x6)
    l1 = x1*V[j]
    L1.append(l1)
    l2 = x2*V[j]
    L2.append(l2)
    l3 = x3*V[j]
    L3.append(l3)
    l4 = x4*V[j]
    L4.append(l4)
    l5 = x5*V[j]
    L5.append(l5)
    l6 = x6*V[j]
    L6.append(l6)
for j in range (len(V)):
    p1 = Vander(V[j],aclap,bclap,T[0]*R2)
    P1.append(p1)
    p2 = Vander(V[j],aclap,bclap,T[1]*R2)
    P2.append(p2)
    p3 = Vander(V[j],aclap,bclap,T[2]*R2)
    P3.append(p3)
    p4 = Vander(V[j],aclap,bclap,T[3]*R2)
    P4.append(p4)
    p5 = Vander(V[j],aclap,bclap,T[4]*R2)
    P5.append(p5)
    p6 = Vander(V[j],aclap,bclap,T[5]*R2)
    P6.append(p6)
    l7 = p1*V[j]
    L7.append(l7)
    l8 = p2*V[j]
    L8.append(l8)   
    l9 = p3*V[j]
    L9.append(l9)
    l10 = p4*V[j]
    L10.append(l10)
    l11 = p5*V[j]
    L11.append(l11)
    l12 = p6*V[j]
    L12.append(l12)
py.plot(X1,L1,color="red",linewidth=1.5, linestyle="-",label='Gaz parfait')
py.plot(X2,L2,color="red",linewidth=1.5, linestyle="-")
py.plot(X3,L3,color="red",linewidth=1.5, linestyle="-")
py.plot(X4,L4,color="red",linewidth=1.5, linestyle="-")
py.plot(X5,L5,color="red",linewidth=1.5, linestyle="-")
py.plot(X6,L6,color="red",linewidth=1.5, linestyle="-")
py.plot(P1,L7,color="blue",linewidth=1.5, linestyle="-",label='Van Der Waals')
py.plot(P2,L8,color="blue",linewidth=1.5, linestyle="-")
py.plot(P3,L9,color="blue",linewidth=1.5, linestyle="-")
py.plot(P4,L10,color="blue",linewidth=1.5, linestyle="-")
py.plot(P5,L11,color="blue",linewidth=1.5, linestyle="-")
py.plot(P6,L12,color="blue",linewidth=1.5, linestyle="-")
py.plot(xval,yval,color="green",linewidth=1.5, linestyle="-",label ='Parabole de Mariotte')
py.scatter([0.7*10**7,],[780,], 50, color ='maroon')
py.annotate('Point critique', xy=(0.7*10**7, 780), xytext=(0.85*10**7,2000), arrowprops=dict(arrowstyle="->"))
py.legend(loc='upper right')
py.show()