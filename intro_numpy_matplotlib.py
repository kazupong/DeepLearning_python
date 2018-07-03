#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 13:59:03 2018

@author: kazoo

O'REILLY JAPAN

"ゼロから作る　Deep Learning"
〜pythonで学ぶディープラーニングの理論と実装〜

reference:
    https://matplotlib.org/2.1.1/api/_as_gen/matplotlib.pyplot.plot.html

 
"""

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)

y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,label = "sin")
plt.plot(x,y2,linestyle = '--' ,label = "cos")

plt.show()
