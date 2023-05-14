# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:12:01 2023

@author: Nour
"""

import matplotlib.pyplot as py
import numpy as np

def PotentielDeLennardJones (x):
    return((((x)**-12)-2*(x)**-6))
def EnergiePotentielleRepulsive(x):
    return((x)**-12)
def EnergiePotentielleAttractive (x):
    return(-2*(x)**-6)

py.figure(figsize=(20,6), dpi=80)
py.subplot(1,2,1)
py.title("Potentiel de Lennard Jones")
ax = py.gca()
ax.set_xlabel('r/r0')
ax.set_ylabel('F/Fo')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0.5))

ax.grid(True)
py.xlim(0.5,2.5)
py.ylim(-1.5,1.5)
py.xticks(np.linspace(0.5,2.5,11,endpoint=True))
py.yticks(np.linspace(-1.5,1.5,7,endpoint=True))

X = np.linspace(0.5, 2.5, 256,endpoint=True)
E=PotentielDeLennardJones(X)
Er=EnergiePotentielleRepulsive(X)
Ea=EnergiePotentielleAttractive(X)
py.plot(X, E, color="blue", linewidth=1.5, linestyle="-",label="Somme des forces")
py.plot(X, Er, color="red", linewidth=1.5, linestyle="-",label="Force répulsive")
py.plot(X, Ea, color="black", linewidth=1.5, linestyle="-",label="Force attractive")
py.scatter([0,],[0,], 200, color ='orange')
py.scatter([0.5,],[0,], 200, color ='red')
py.scatter([0.9,],[0,], 200, color ='red')
py.scatter([1.75,],[-0.1,], 200, color ='red')
py.scatter([2.25,],[0,], 200, color ='red')
py.scatter([0.6,],[-1.25,], 200, color ='green')
py.scatter([0.7,],[-1.25,], 200, color ='purple')
py.scatter([0.9,],[-1.25,], 200, color ='purple')
py.scatter([1.1,],[-1.25,], 200, color ='purple')
py.scatter([1.3,],[-1.25,], 200, color ='purple')
py.annotate('', xy=(0.91, -0.5), xytext=(0.9,0), arrowprops={'facecolor':'black', 'shrink':0.1})
py.annotate('', xy=(1.5, -0.14), xytext=(1.75,-0.1), arrowprops={'facecolor':'black', 'shrink':0.1})
py.annotate('', xy=(0.85, -1.25), xytext=(0.7,-1.25), arrowprops={'facecolor':'black', 'shrink':0.1})
py.annotate('', xy=(0.95, -1.25), xytext=(1.1,-1.25), arrowprops={'facecolor':'black', 'shrink':0.1})
py.annotate('', xy=(1.15, -1.25), xytext=(1.3,-1.25), arrowprops={'facecolor':'black', 'shrink':0.1})
répulsive=py.axvspan(0, 0.89,facecolor='m',alpha=0.3)
py.legend(loc='upper right')
py.show()