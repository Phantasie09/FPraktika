import numpy
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sci
from matplotlib.backend_bases import MouseButton
import matplotlib as mpl
mpl.use('TkAgg')
#3

path= "OpticsPlasma/F407_backup"
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
boocounter = False
arrowsvis = []
arrowdata =[]
P1, P2 = [0.1, 0.2], [0.9, 0.5]





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

    def calculateslope():
        slopesss=[]
        for i in arrowdata:
            slope= (i[1][1]-i[0][1])/(i[1][0]-i[0][0])
            slopesss.append(slope)

            print(slope)
        print(np.std(slopesss))
        print(np.mean(slopesss))

    def on_key(event):
        if event.key == "x" and len(arrowsvis) != 0:
            helper = arrowsvis.pop()
            arrowdata.pop()
            helper.remove()
            plt.show()

        if event.key == "p" and len(arrowdata) != 0:
            calculateslope()


    def drawarrow(event):
        global P1, P2, boocounter, arrows
        if event.button == MouseButton.LEFT:
            if boocounter == False:
                P1[0] = event.xdata
                P1[1] = event.ydata
                print("first")
            else:
                P2[0] = event.xdata
                P2[1] = event.ydata
                arrow = ax1.annotate("", xy=(P2[0], P2[1]), xytext=(P1[0], P1[1]),
                                    arrowprops=dict(arrowstyle="->", color="k", connectionstyle=" arc3 "))
                arrowsvis.append(arrow)

                arrowdata.append([[P1[0],P1[1]],[P2[0],P2[1]]])
                print(arrowdata)
                print(f'data coords {event.xdata} {event.ydata},',
                      f'pixel coords {event.x} {event.y}')

            boocounter = not boocounter

            plt.show()

    binding_id = plt.connect('key_press_event', on_key)
    plt.connect('button_press_event', drawarrow)


    plt.show()
    #fig.savefig('finalGraphs/'+topicstheme[p]+name+'.png')



werteAus(0,'2.1.10pa')

