# -*- coding: utf-8 -*-
"""
Created on Sat May 13 11:06:10 2023

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
py.plot(X, E, color="green", linewidth=1.5, linestyle="-",label="Energie d'interaction réduite totale")
py.plot(X, Er, color="blue", linewidth=1.5, linestyle="-",label="Energie réduite de répulsion")
py.plot(X, Ea, color="red", linewidth=1.5, linestyle="-",label="Energie réduite d'attraction")
attractive = py.axvspan(1, 2, facecolor='b', alpha=0.3, label='Zone attractive')
interraction = py.axvspan(2, 2.5, facecolor='g', alpha=0.3, label='Zone sans interractions')
répulsive = py.axvspan(0, 1, facecolor='r', alpha=0.3, label='Zone répulsive')
py.annotate("", xy=(0.5, 0.2), xytext=(1, 0.2), arrowprops=dict(arrowstyle="<->"))
py.annotate("", xy=(1.0, 0.0), xytext=(1, -1.0), arrowprops=dict(arrowstyle="<->"))
py.text(0.7, .22, r'r = r0')
py.text(1.01, -0.5, r"Position d'équilibre")
py.legend(loc='upper right')
py.show()
