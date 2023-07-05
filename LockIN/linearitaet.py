# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 16:10:05 2023

@author: HP-Notebook
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

Ui = [20, 50, 100, 200, 500, 1000]
Uo = [3.0, 12, 31, 56, 160, 290]
fui = [1, 2, 10, 10, 20, 50]
fuo = [0.5, 1, 1, 1, 10, 10]

y= np.array([3.0, 12, 31, 56, 160, 290])
x= np.array([20, 50, 100, 200, 500, 1000]).reshape((-1,1))

model= LinearRegression(fit_intercept=False).fit(x, y)
r_sq = model.score(x, y)
r= f"R$^{2}$: {r_sq}"

s= f"b: {model.coef_}"

def y(x):
    y= model.coef_ *x
    return y


plt.plot(Ui, y(Ui), label='Lineare Regression y=b*x \n'+r+'\n' + s)
#plt.scatter(Uo, Ui)
plt.errorbar(Ui, Uo, yerr=(fuo), xerr=(fui), fmt='none', color='black', label='Daten')
plt.ylabel('U$_{out}$/mV')
plt.xlabel('U$_{in}$/mV')
plt.legend()
plt.show()