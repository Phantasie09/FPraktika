# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np

at = [1, 0.333, 0.200, 0.143, 0.111, 0.091, 0.079, 0.067, 0.059]
am = [1, 0.355, 0.200, 0.141, 0.112, 0.089, 0.079, 0.071, 0.056]
f = [1, 3, 5, 7, 9, 11, 13, 15, 17]

t= np.linspace(0, 2, num=1000)

def ft(n,x):
    y = (4/np.pi)*at[n]*np.sin(2*np.pi*f[n]*x)
    return y


def fm(n,x):
    z = (4/np.pi)*am[n]*np.sin(2*np.pi*f[n]*x)
    return z


plt.plot(t, sum(ft(n,t) for n in range(0,8)))
plt.xlabel("t/s")
plt.ylabel("R(t)/V")
plt.plot(t, sum(fm(n,t) for n in range(0,8)))
plt.show()


