import numpy as np
import matplotlib.pyplot as plt


delta = 0.25
x, y = np.arange(-2, 2, delta), np.arange(-2, 2, delta)
vx, vy = np.meshgrid(np.cos(x) * np.sin(y), -np.sin(x) * np.cos(y))


plt.figure()
plt.quiver(x, y, vx, vy)
plt.savefig('oppg3.png')
