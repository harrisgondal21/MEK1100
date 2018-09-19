import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

data = sio.loadmat("data.mat")
x = data.get("x")
y = data.get("y")
u = data.get("u")
v = data.get("v")
xit = data.get("xit")
yit = data.get("yit")

def draw_rects():
    ## Rect 1
    corner1 = (x[159, 34], y[159, 34])
    corner2 = (x[169, 69], y[169, 69])

    plt.plot([corner1[0], corner1[0]], [corner1[1], corner2[1]], "k")
    plt.plot([corner2[0], corner2[0]], [corner1[1], corner2[1]], "g")
    plt.plot([corner1[0], corner2[0]], [corner1[1], corner1[1]], "r")
    plt.plot([corner1[0], corner2[0]], [corner2[1], corner2[1]], "b")

    ## Rect 2
    corner1 = (x[84, 34], y[84, 34])
    corner2 = (x[99, 69], y[99, 69])

    plt.plot([corner1[0], corner1[0]], [corner1[1], corner2[1]], "k")
    plt.plot([corner2[0], corner2[0]], [corner1[1], corner2[1]], "g")
    plt.plot([corner1[0], corner2[0]], [corner1[1], corner1[1]], "r")
    plt.plot([corner1[0], corner2[0]], [corner2[1], corner2[1]], "b")

    ## Rect 3
    corner1 = (x[49, 34], y[49, 34])
    corner2 = (x[59, 69], y[59, 69])

    plt.plot([corner1[0], corner1[0]], [corner1[1], corner2[1]], "k")
    plt.plot([corner2[0], corner2[0]], [corner1[1], corner2[1]], "g")
    plt.plot([corner1[0], corner2[0]], [corner1[1], corner1[1]], "r")
    plt.plot([corner1[0], corner2[0]], [corner2[1], corner2[1]], "b")


## Oppgave C:
plt.figure()

draw_rects()

plt.plot(xit, yit, "b*")
skip_num = 5
plt.quiver(x[::skip_num, ::skip_num], y[::skip_num, ::skip_num], u[::skip_num, ::skip_num], v[::skip_num, ::skip_num])

plt.show()

## Oppgave D:

plt.figure()

dudx = np.gradient(u, axis=0)
dvdy = np.gradient(v, axis=1)


div = dudx + dvdy

plt.subplot(2, 1, 1)

draw_rects()

divergence = plt.contourf(x, y, div)
plt.colorbar(divergence)

plt.plot(xit, yit, "k*")

## Oppgave E:

dudy = np.gradient(u, axis=1)
dvdx = np.gradient(v, axis=0)

curl = dvdx - dudy

plt.subplot(2, 1, 2)

draw_rects()

vir = plt.contourf(x, y, curl)
plt.colorbar(vir)

plt.plot(xit, yit, "k*")
plt.show()

## Oppgave F:

def f(y, x):
    return u + v

def bounds_x():
    return [17.0, 34.5]
def bounds_y():
    return [29.5, 34.5]

print integrate.dblquad(f, 17.0, 34.5, lambda x: 29.5, lambda y: 34.5)