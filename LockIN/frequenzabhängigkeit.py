# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 07:19:57 2023

@author: HP-Notebook
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

f = [2000, 1000, 500, 200, 100, 50, 35, 20]
Uo = [32, 34.2, 34.5, 34.7, 34, 33, 33, 30]
ff = [250, 25, 5, 5, 5, 0.5, 0.5, 0.5]
fuo = [1, 0.1, 0.1, 0.1, 1, 1, 1, 5]



#plt.plot(f, Uo, label='Daten')
plt.scatter(f, Uo, label='Messpunkte')
plt.errorbar(f, Uo, yerr=fuo, xerr=ff, fmt='none', color='black')
plt.ylabel('U$_{out}$/mV')
plt.xlabel('f/Hz')
plt.legend()
plt.show()
