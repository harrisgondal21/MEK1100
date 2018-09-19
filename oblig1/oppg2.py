import numpy as np
import matplotlib.pylab as plt

N = 1000

x = np.linspace(-2, 2, N)
y = np.linspace(-2, 2, N)

x, y = np.meshgrid(x, y)
z = np.log(np.abs(x)) - y

plt.contour(x, y, z)
plt.savefig("oppg2.png")
plt.show()
