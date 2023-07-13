import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sci

path="../OpticsPlasma/F407_backup"
files="/7.05 TimKatharinae/"
dnamen=["2.1.10pa","2.1.20pa","2.1.40pa","2.1.60pa"]
vnamen=["2.1.350V","2.1.450V","2.1.550V","2.1.650V"]
pnamen=["2.2.20porzent","2.2.50prozent","2.2.75prozent","2.2.100prozent"]
topicstheme=["druck","volt","mischung"]
topics=[dnamen,vnamen,pnamen]
#Konstanten
tau_neon=14.5*10**(-9)
tau_h2=5

"""
for p in range(0,3):
    for name in topics[p]:
        for i in range(0,20):
            localpath=topicstheme[p]+"/"+name + "/Image_time_" + str(i + 1) +"median"+ ".npy"
            t=np.load(localpath)
"""
p=0
i=0
name="2.1.10pa"
helper=[]
for i in range(0,20):
    localpath=topicstheme[p]+"/"+name + "/Image_time_" + str(i + 1) +"median"+ ".npy"
    t=np.load(localpath)
    f=np.gradient(t)
    energy = (f + 1 / tau_neon * t)
    helper.append(energy)
superduppermatrix=np.array(helper)
superduppermatrix=superduppermatrix.transpose()[::-1]
superduppermatrix=superduppermatrix[:137]


M=np.array(superduppermatrix)
print(M.shape)
sigma = 0.8

M = sci.filters.gaussian_filter(M, sigma)
M = sci.zoom(M, 3)
fig, ax1 = plt.subplots(layout='constrained')
ax1.contour(M, levels=10, linewidths=0.5, colors='k')
ax1.set_title('grid and contour (%d points, %d grid points)'
              )

cntr1 = ax1.contourf(M, levels=10, cmap="RdBu_r")

fig.colorbar(cntr1, ax=ax1)
plt.show()





