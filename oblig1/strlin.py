import matplotlib.pyplot as plt
from streamfun import streamfun

#n = 5
x_5, y_5, psi_5 = streamfun(5)

#n = 50
x_50, y_50, psi_50 = streamfun(50)


plt.figure()
plt.subplot(211)
contour_plot = plt.contour(x_5, y_5, psi_5)
plt.clabel(contour_plot, inline=1, fontsize=10)
plt.title('n = 5')


plt.subplot(212)
contour_plot_2 = plt.contour(x_50, y_50, psi_50)
plt.clabel(contour_plot_2, inline=1, fontsize=10)
plt.title('n = 50')
plt.savefig('strlin.png')

plt.show()
