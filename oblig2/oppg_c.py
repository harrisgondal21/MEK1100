import scipy.io as sio
import matplotlib.pylab as plt

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

plt.figure()

draw_rects()

plt.plot(xit, yit, "b*")
skip_num = 5
plt.quiver(x[::skip_num, ::skip_num], y[::skip_num, ::skip_num], u[::skip_num, ::skip_num], v[::skip_num, ::skip_num])

plt.savefig("oppg_c.png")
plt.show()