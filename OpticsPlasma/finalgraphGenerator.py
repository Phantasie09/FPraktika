import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sci
import datenanalyse

path="../OpticsPlasma/F407_backup"
files="/7.05 TimKatharinae/"
dnamen=["2.1.10pa","2.1.20pa","2.1.40pa","2.1.60pa"]
vnamen=["2.1.350V","2.1.450V","2.1.550V","2.1.650V"]
pnamen=["2.2.20porzent","2.2.50prozent","2.2.75prozent","2.2.100prozent"]
topicstheme=["druck","volt","mischung"]
topics=[dnamen,vnamen,pnamen]
t=0
for p in range(0,3):
    for name in topics[p]:
            if t==0:
                t = int(input("press 1 or 2 to run all to proceed else exit: "))
            if t==1:
                print("weiter mit file: "+name)
                datenanalyse.werteAus(p, name=name)
                t=0
            elif t==2:
                print("weiter mit file"+name)
                #datenanalyse.werteAus(p, name=name)
            else:
                print("exit")
                exit()
            #
