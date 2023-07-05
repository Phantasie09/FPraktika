# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 23:34:00 2023

@author: HP-Notebook
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

f = [44, 100, 200, 500, 700]
Uo = [8.5, 8.55, 8.54, 8.53, 8.5]
ff = [1, 5, 5, 5, 5]
fuo = [0.1, 0.01, 0.01, 0.01, 0.01]



#plt.plot(f, Uo, label='Daten')
plt.scatter(f, Uo, label='Messpunkte')
plt.errorbar(f, Uo, yerr=fuo, xerr=ff, fmt='none', color='black')
plt.ylabel('U$_{out}$/mV')
plt.xlabel('f/Hz')
plt.legend()
plt.show()
