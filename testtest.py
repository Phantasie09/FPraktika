import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as sci
import math

spacing_b=5 *10**(-2) #meter
number_wire=2 #Defines Room spacing_b*number_wire
length=500 #meter
room=number_wire*spacing_b
Voltage=500 #Volt anahme lektronen Kannoe
em_ver=1.7*10**9
v_x= np.sqrt(2*em_ver*Voltage)
current_wire=500 #Ampeer
mu=1.256*10**(-6)
testobj=v_x*np.random.rand(20)


posyn=np.random.rand()/2
v_y=0
stepnum=10*7


stepsize=length/stepnum

step =np.arange(0,stepnum)

peak_v = [1] * (len(step))
peak_p=[1] * (len(step))

for v_x in testobj:
    posy = 0.09050568880368716
    stepptime = stepsize / v_x
    values_vy = [v_y] * (len(step))
    values_py = [posy] * (len(step))
    usless=False
    for i in range(len(step)):
        v_y=v_y+stepptime*em_ver*mu*1/(2* math.pi)*current_wire*(1/posy-1/(room-posy))
        posy=posy+stepptime*v_y
        if(posy<0 or posy>room):
            usless=True
            break
        values_vy[i]=v_y
        values_py[i]=posy
    if(usless==False):
        peak_v[i]= max(values_vy)-min(values_vy)
        peak_p[i]=max(values_py) - min(values_py)
    fig, axs = plt.subplots(2)
    fig.suptitle('Speed:'+str(v_x))
    axs[0].set_title("pos")
    axs[0].plot(step, values_py)
    axs[1].plot(step, values_vy)
list(filter(lambda num: num != 0, peak_v))
list(filter(lambda num: num != 0, peak_p))
#fig2, axs2 = plt.subplots(1)
#axs2.set_title("pos")
#axs2.plot(peak_v,peak_v)

#fig2.suptitle('Amplitude:'+str(v_x))
plt.show()

print(peak_p)
print(peak_v)