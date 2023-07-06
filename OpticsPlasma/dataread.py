import numpy as np

import os
path="../OpticsPlasma/F407_backup"
files="/7.05 TimKatharine/"
dnamen=["2.1.10pa","2.1.20pa","2.1.40pa","2.1.60pa"]
vnamen=["2.1.350V","2.1.450V","2.1.550V","2.1.650V"]
pnamen=["2.2.20porzent","2.2.50prozent","2.2.75prozent","2.2.100prozent"]
topicstheme=["druck","volt","mischung"]
topics=[dnamen,vnamen,pnamen]

for p in range(0,3):
    for name in topics[p]:
        if not os.path.exists(topicstheme[p]+"/"+name):
            os.makedirs(topicstheme[p]+"/"+name)
        t=np.loadtxt(path+files+name+".asc")
        for i in range(0,19):
            y=    np.array(t[0 + i * 1024:+(i + 1) * 1024])
            #x=np.delete(y,0,1)
            np.save(topicstheme[p]+"/"+name + "/Image_time_" + str(i + 1) + ".npy", y)



