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
py.title("Isotherme d'un gaz parfait et d'un fluide de Van Der")
ax.set_xlabel('Volume molaire',labelpad = 10)
ax.set_ylabel('Pression',labelpad = 10)
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
py.grid(True)
py.xlim(0,0.0010)
py.ylim(0,30000000)
V = [p/100000 for p in range (1,110)]
T = [t for t in range(300,1301,200)]
for j in range (len(V)):
    p1 = EquationGazParfait(V[j],T[0],R2)
    P1.append(p1)
    p2 = EquationGazParfait(V[j],T[1],R2)
    P2.append(p2)
    p3 = EquationGazParfait(V[j],T[2],R2)
    P3.append(p3)
    p4 = EquationGazParfait(V[j],T[3],R2)
    P4.append(p4)
    p5 = EquationGazParfait(V[j],T[4],R2)
    P5.append(p5)
    p6 = EquationGazParfait(V[j],T[5],R2)
    P6.append(p6)
for j in range (len(V)):
    f1 = Vander(V[j],aclap,bclap,T[0]*R2)
    F1.append(f1)
    f2 = Vander(V[j],aclap,bclap,T[1]*R2)
    F2.append(f2)
    f3 = Vander(V[j],aclap,bclap,T[2]*R2)
    F3.append(f3)
    f4 = Vander(V[j],aclap,bclap,T[3]*R2)
    F4.append(f4)
    f5 = Vander(V[j],aclap,bclap,T[4]*R2)
    F5.append(f5)
    f6 = Vander(V[j],aclap,bclap,T[5]*R2)
    F6.append(f6)
py.plot(V,P1,color="purple",linewidth=1.5, linestyle="-",label='Gaz parfait')
py.plot(V,P2,color="purple",linewidth=1.5, linestyle="-")
py.plot(V,P3,color="purple",linewidth=1.5, linestyle="-")
py.plot(V,P4,color="purple",linewidth=1.5, linestyle="-")
py.plot(V,P5,color="purple",linewidth=1.5, linestyle="-")
py.plot(V,P6,color="purple",linewidth=1.5, linestyle="-")
py.plot(V,F1,color="Green",linewidth=1.5, linestyle="-",label='Van Der Waals')
py.plot(V,F2,color="Green",linewidth=1.5, linestyle="-")
py.plot(V,F3,color="Green",linewidth=1.5, linestyle="-")
py.plot(V,F4,color="Green",linewidth=1.5, linestyle="-")
py.plot(V,F5,color="Green",linewidth=1.5, linestyle="-")
py.plot(V,F6,color="Green",linewidth=1.5, linestyle="-")
py.legend(loc='upper right')
py.show()