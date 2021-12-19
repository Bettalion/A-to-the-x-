import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D 
import numpy as np
plt.rcParams['figure.figsize']=(8,5)
fig = plt.figure('Mapping Im & Re')
ax = Axes3D(fig)

np.random.seed(31)

mu = 30
n = 10 #range of x

x = np.array(list(range(-n,n)))
# print(x.shape)
print(x)
y = np.array(list(map(
  lambda x: 2*x + 10,x       # <--- equ for y
    )))
# z = np.random.normal(mu,1, size=n)
z = np.array(list(map(
  lambda x: -x+1,x       # <--- equ for z
    )))
print(y,z)



ax.scatter3D(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()


