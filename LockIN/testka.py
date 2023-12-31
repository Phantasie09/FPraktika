import matplotlib.pyplot as plt
import numpy as np

at = [1, 0.333, 0.200, 0.143, 0.111, 0.091, 0.079, 0.067, 0.059]
am = [1, 0.355, 0.200, 0.141, 0.112, 0.089, 0.079, 0.071, 0.056]
f = [1, 3, 5, 7, 9, 11, 13, 15, 17]

x= np.arange(0, 3, 0.1)

def ft(u):
    y = 4/np.pi*np.array([at[n]*np.sin(1/(2*n+1)*2*np.pi*f[n]*u) for n in range(0,8)])
    return y.sum()

def fm(t):
    z = 4/np.pi*np.array([am[n]*np.sin(1/(2*n+1)*2*np.pi*f[n]*t) for n in range(0,8)])
    return z.sum()


y1= [ft(p) for p in x  ]
y2=[fm(p) for p in x  ]
plt.plot(x, y1,color='b',linestyle='-')
plt.plot(x, y2,color='r',linestyle='--')
plt.xlabel("t/s")
plt.ylabel("R(t)/V")


plt.title('4b',fontsize=18)
plt.legend()
plt.savefig("speed-data-nyc.eps", bbox_inches='tight')
plt.show()


































































































































































































































































































































































































































































































