import numpy as np
#2
path="../OpticsPlasma/F407_backup"
files="/7.05 TimKatharinae/"
dnamen=["2.1.10pa","2.1.20pa","2.1.40pa","2.1.60pa"]
vnamen=["2.1.350V","2.1.450V","2.1.550V","2.1.650V"]
pnamen=["2.2.20porzent","2.2.50prozent","2.2.75prozent","2.2.100prozent"]
topicstheme=["druck","volt","mischung"]
topics=[dnamen,vnamen,pnamen]

#2

for p in range(0,3):
    for name in topics[p]:
        for i in range(0,20):
            localpath=topicstheme[p]+"/"+name + "/Image_time_" + str(i + 1) + ".npy"
            t=np.load(localpath)
            if t.size<=100:
                raise Exception("Sorry, already done")
                break
            bet=t[290:713] #Pixel 289 bis 372
            transpose = bet.transpose()
            transpose = transpose[136:-2]
            median = []
            for lol in transpose:
                kappa = sum(lol) / 425
                median.append(kappa)
            newpath = topicstheme[p] + "/" + name + "/Image_time_" + str(i + 1) +"median"+ ".npy"
            np.save(newpath, median)
#AUfaddieren der  Spalten


