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

## Oppgave E:

dudy = np.gradient(u, axis=1)
dvdx = np.gradient(v, axis=0)

curl = dvdx - dudy

draw_rects()

vir = plt.contourf(x, y, curl)
plt.colorbar(vir)

plt.plot(xit, yit, "k*")

plt.savefig("oppg_e.png")
plt.show()