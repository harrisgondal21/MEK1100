import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

data = sio.loadmat("data.mat")
x = data.get("x")
y = data.get("y")
u = data.get("u")
v = data.get("v")
xit = data.get("xit")
yit = data.get("yit")

plt.figure()

dudx = np.gradient(u, axis=0)
dvdy = np.gradient(v, axis=1)


div = dudx + dvdy

draw_rects()

divergence = plt.contourf(x, y, div)
plt.colorbar(divergence)

plt.plot(xit, yit, "k*")

plt.savefig("oppg_d.png")
plt.show()