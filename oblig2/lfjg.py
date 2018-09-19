import matplotlib.pylab as plt
import numpy as np

delta = 0.5
x, y = np.meshgrid(np.arange(-5, 5, delta), np.arange(-5, 5, delta))
vx, vy = x * y**2, -x**2 * y

plt.quiver(x, y, vx, vy)
plt.show()