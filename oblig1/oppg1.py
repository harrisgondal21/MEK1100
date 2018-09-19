import numpy as np
import matplotlib.pylab as plt

n = 0
N = 1000

t = np.linspace(0, 1, N)
x = np.zeros(N)
y = np.zeros(N)

##Init
v0 = 1.0
theta = [np.pi/10, np.pi/4, np.pi/3]

for n in range(3):
    for i in range(N):
        x[i] = t[i]
        y[i] = x[i]*np.tan(theta[n])*(1-t[i])

    plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.legend(["pi/10", "pi/4", "pi/3"])
plt.savefig("oppg1.png")
plt.show()
