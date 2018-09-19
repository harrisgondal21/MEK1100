import scipy.io as sio
import numpy as np

data = sio.loadmat("data.mat")
x = data.get("x")
y = data.get("y")
u = data.get("u")
v = data.get("v")
xit = data.get("xit")
yit = data.get("yit")

print np.shape(x)
print np.shape(y)
print np.shape(u)
print np.shape(v)
print np.shape(xit)
print np.shape(yit)
print x
print y

"""
1x-193:oblig2 joakimflatby$ python oppg_a.py
(201, 194)
(201, 194)
(201, 194)
(201, 194)
(1, 194)
(1, 194)
[[  0.    0.5   1.  ...,  95.5  96.   96.5]
 [  0.    0.5   1.  ...,  95.5  96.   96.5]
 [  0.    0.5   1.  ...,  95.5  96.   96.5]
 ...,
 [  0.    0.5   1.  ...,  95.5  96.   96.5]
 [  0.    0.5   1.  ...,  95.5  96.   96.5]
 [  0.    0.5   1.  ...,  95.5  96.   96.5]]
[[-50.  -50.  -50.  ..., -50.  -50.  -50. ]
 [-49.5 -49.5 -49.5 ..., -49.5 -49.5 -49.5]
 [-49.  -49.  -49.  ..., -49.  -49.  -49. ]
 ...,
 [ 49.   49.   49.  ...,  49.   49.   49. ]
 [ 49.5  49.5  49.5 ...,  49.5  49.5  49.5]
 [ 50.   50.   50.  ...,  50.   50.   50. ]]
"""