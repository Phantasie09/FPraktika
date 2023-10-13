import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.use('TkAgg')
from matplotlib.backend_bases import MouseButton

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)

arrows=[]
P1,P2=[0.1,0.2],[0.9,0.5]

def on_key(event):
    if event.key == "x" and len(arrows) != 0:
        helper=arrows.pop()
        helper.remove()
        plt.show()
        print(arrows)

boocounter=False
def drawarrow(event):
    global P1,P2, boocounter,arrows
    if event.button== MouseButton.LEFT:
        if boocounter == False:
            P1[0] =event.xdata
            P1[1] =event.ydata
            print("first")
        else:
            P2[0] = event.xdata
            P2[1] = event.ydata
            arrow=ax.annotate("", xy=(P2[0], P2[1]), xytext=(P1[0], P1[1]),
                        arrowprops=dict(arrowstyle="->", color="k", connectionstyle=" arc3 "))
            arrows.append(arrow)
            print(f'data coords {event.xdata} {event.ydata},',
                  f'pixel coords {event.x} {event.y}')

        boocounter= not boocounter

        plt.show()

binding_id = plt.connect('key_press_event', on_key)
plt.connect('button_press_event', drawarrow)
plt.show()
