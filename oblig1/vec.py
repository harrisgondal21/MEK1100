from velfield import velfield
import matplotlib.pyplot as plt

x, y, vx, vy = velfield(10)

plt.figure()
plt.quiver(x, y, vx, vy, 1.5)
plt.savefig('velfield.png')
