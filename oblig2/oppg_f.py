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

## Kurveintegral
rect1_sides = np.zeros(4)
for i in u[159, 34:70]:
    rect1_sides[2] += i*0.5
for i in v[159:170, 69]:
    rect1_sides[1] += i*0.5
for i in u[169, 34:70]:
    rect1_sides[0] -= i*0.5
for i in v[159:170, 34]:
    rect1_sides[3] -= i*0.5


rect2_sides = np.zeros(4)
for i in u[84, 34:70]:
    rect2_sides[2] += i*0.5
for i in v[84:100, 69]:
    rect2_sides[1] += i*0.5
for i in u[99, 34:70]:
    rect2_sides[0] -= i*0.5
for i in v[84:100, 34]:
    rect2_sides[3] -= i*0.5

rect3_sides = np.zeros(4)
for i in u[49, 34:70]:
    rect3_sides[2] += i*0.5
for i in v[49:60, 69]:
    rect3_sides[1] += i*0.5
for i in u[59, 34:70]:
    rect3_sides[0] -= i*0.5
for i in v[49:60, 34]:
    rect3_sides[3] -= i*0.5


rect1 = sum(rect1_sides)
rect2 = sum(rect2_sides)
rect3 = sum(rect3_sides)

print "Rect 1: %f" %(rect1)
print "Rect 2: %f" %(rect2)
print "Rect 3: %f" %(rect3)

"""
1x-193:oblig2 joakimflatby$ python oppg_f.py
Rect 1: 2695.514093
Rect 2: -60976.600162
Rect 3: 9.521016

"""

## Flateintegral

def flate(x1,x2,y1,y2):
    curl = (np.gradient(v,axis=0))-(np.gradient(u,axis=1))
    s = 0
    for i in range (y1,y2):
        for j in range (x1,x2):
            s += curl[i,j]*0.25
    return s

print "Rect 1: %f" %(flate(34, 69, 159, 169))
print "Rect 2: %f" %(flate(34, 69, 84, 99))
print "Rect 3: %f" %(flate(34, 69, 49, 59))

"""
Rect 1: -700.923318
Rect 2: -6505.544669
Rect 3: 139.104254
"""