import numpy as np
import matplotlib.pyplot as plt

path="../OpticsPlasma/F407_backup"
files="/7.05 TimKatharinae/"
dnamen=["2.1.10pa","2.1.20pa","2.1.40pa","2.1.60pa"]
vnamen=["2.1.350V","2.1.450V","2.1.550V","2.1.650V"]
pnamen=["2.2.20porzent","2.2.50prozent","2.2.75prozent","2.2.100prozent"]
topicstheme=["druck","volt","mischung"]
topics=[dnamen,vnamen,pnamen]
"""
for p in range(0,3):
    for name in topics[p]:
        for i in range(0,20):
            localpath=topicstheme[p]+"/"+name + "/Image_time_" + str(i + 1) +"median"+ ".npy"
            t=np.load(localpath)
"""
p=0
i=5
name="2.1.10pa"
localpath=topicstheme[p]+"/"+name + "/Image_time_" + str(i + 1) + ".npy"
t=np.load(localpath)
bet=t[240:772]
trans=bet.transpose()
spieg=trans[::-1]



plt.imshow(spieg,interpolation='nearest')
#plt.plot(t,  label='theoretisch')
plt.xlabel("t/s")
plt.ylabel("R(t)/V")
plt.legend(loc='lower right')
plt.show()