import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sci

#3

path="../OpticsPlasma/F407_backup"
files="/7.05 TimKatharinae/"
dnamen=["2.1.10pa","2.1.20pa","2.1.40pa","2.1.60pa"]
vnamen=["2.1.350V","2.1.450V","2.1.550V","2.1.650V"]
pnamen=["2.2.20porzent","2.2.50prozent","2.2.75prozent","2.2.100prozent"]
topicstheme=["druck","volt","mischung"]
topics=[dnamen,vnamen,pnamen]
#Konstanten
tau_neon=14.5*10**(-9)
tau_h2=10.2*10**(-9)
tau=[tau_h2,tau_h2,tau_neon]
def werteAus(p,name):
    helper=[]
    for i in range(0,20):
        localpath=topicstheme[p]+"/"+name + "/Image_time_" + str(i + 1) +"median"+ ".npy"
        timstampt=np.load(localpath)
        helper.append(timstampt)
    trans_helper=np.array(helper).transpose()
    superduppermatrix=[]
    for t in trans_helper:
        f = np.gradient(t, 10 ** (-8), edge_order=1)
        """
        ab = []
        for i in range(len(t) - 1):
            ab.append((t[i + 1] - t[i]) / 10 ** (-8))
        ab.append(ab[-1])
        plt.plot(ab)
        plt.plot(f)
        plt.show()
        """ #Zur Kontrolle ob gradient funktioniert
        energy = (f + 1 / tau_neon * t)
        superduppermatrix.append(energy)



    M=np.array(superduppermatrix)  #x Pixel 0,023529412cm y Pixel 5ns
    sigma = 0.8
    M_filter = sci.filters.gaussian_filter(M, sigma)
    M_filter2 = sci.zoom(M_filter, 3)
    #M_filter2 = M




    maximalValue=M_filter2.max()
    minmalValue= M_filter2.min()

    pos=np.argwhere(M_filter2==maximalValue)
    M_filter2=(M_filter2-minmalValue)/(maximalValue-minmalValue)



    pixtomm= 0.023529412 * ( M.shape[0] / M_filter2.shape[0] )


    feature_x=np.linspace(0,20*5, M_filter2.shape[1])
    feature_y=np.linspace(0,M_filter2.shape[0]*pixtomm,M_filter2.shape[0])

    [X, Y] = np.meshgrid(feature_x, feature_y)


    fig, ax1 = plt.subplots(layout='constrained')
    ax1.contour(X,Y,M_filter2, levels=10,
                linewidths=0.5, colors='k')
    cntr1 = ax1.contourf(X,Y, M_filter2, levels=10,
                         cmap="inferno") #RdYlBu
    ax1.hlines(pos[0][0]*pixtomm,0,100,colors="black")
    fig.colorbar(cntr1, ax=ax1)
    ax1.tick_params(bottom=True, top=True, left=True, right=True)
    plt.ylabel("Distance [cm]")
    plt.xlabel("Time [ns]")
    plt.show()
    fig.savefig('finalGraphs/'+topicstheme[p]+name+'.png')
    plt.close()


werteAus(0,'2.1.10pa')

