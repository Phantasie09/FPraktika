import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sci




delta = 0.025
x = np.arange(-6.0, 6.0, delta)
y = np.arange(-6.0, 6.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.sin(X )
Z2 = np.cos(Y)
Z = (Z1 - Z2) * 2







fig, ax1 = plt.subplots(layout='constrained')
CS=ax1.contour(X,Y,Z,  linewidths=0.5, colors='k')
ax1.set_title("grapfen")
#cntr1 = ax1.contourf(X,Y, Z, levels=10, cmap="RdYlBu") #inferno
print(CS.collections[1].__dict__)
po=CS.collections[1].get_paths()[2]
v = po.vertices
x = v[:, 0]
y = v[:, 1]
ax1.plot(x,y)
#fig.colorbar(cntr1, ax=ax1)
ax1.clabel(CS, inline=True, fontsize=10)
plt.ylabel("Distance/cm")
plt.xlabel("time/ns")
plt.show()


plt.close()


