import numpy as np
import matplotlib.pyplot as plt

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
superduppermatrix=superduppermatrix[:135]


plt.imshow(superduppermatrix, cmap='viridis', interpolation='nearest', aspect=0.2)
#plt.pcolormesh( cmap='viridis', interpolation='nearest' )

plt.xticks(np.array(range(20)),np.array(range(20))*5)
plt.xticks(np.arange(0,20, step=2))
#plt.yticks(np.array(range(i)/42))


"""
plt.plot(f)
plt.plot(t)
plt.plot(energy)
#plt.plot(t,  label='theoretisch')
"""
plt.ylabel("Output")
plt.xlabel("time/ns")
#plt.legend(loc='lower right')
plt.show()