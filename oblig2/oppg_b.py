import scipy.io as sio
import numpy as np
import matplotlib.pylab as plt

data = sio.loadmat("data.mat")
x = data.get("x")
y = data.get("y")
u = data.get("u")
v = data.get("v")
xit = data.get("xit")
yit = data.get("yit")

velocity_components = np.sqrt(u**2 + v**2)
plt.figure()

plt.subplot(2, 1, 1)
plt.plot(xit, yit, "k*")
CS = plt.contourf(x, y, velocity_components, np.linspace(0, 500, 100))
plt.colorbar(CS)

plt.subplot(2, 1, 2)
plt.plot(xit, yit, "k*")
CS2 = plt.contourf(x, y, velocity_components, np.linspace(1000, 5000, 100))
plt.colorbar(CS2)

plt.savefig("oppg_b.png")
plt.show()