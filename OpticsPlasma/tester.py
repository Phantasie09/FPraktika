import numpy as np

import matplotlib.pyplot as plt

t=np.array([5,4,3])
g=np.array([1,1,1])

i = 4

arr = np.reshape(np.linspace(0,1,i**2), (i,i))
print(arr)
plt.figure(figsize=(12,4))

plt.subplot(131)

plt.imshow(arr, cmap = 'coolwarm', interpolation='nearest')
plt.xticks(np.arange(0,4)*5.0)

plt.yticks(range(i))

plt.title('Without blending color map', y=1.02, fontsize=12)
plt.show()