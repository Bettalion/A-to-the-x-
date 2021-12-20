import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D 
import numpy as np

Base = -1
n = 10 #range of x
density = 10 # intervals

plt.rcParams['figure.figsize']=(15,7.5)
fig = plt.figure(f'Mapping Im & Re : for {Base}^x, x_domain {n}, density {density}')
ax = Axes3D(fig)


x = np.array(list(map(lambda x: x/density,range(n*density))),dtype=complex) # ,dtype=complex means that the array understands it is a complex number and not Nan
# print(x.shape)
# print(x)
y = np.array(list(map(
  lambda y: (Base**y).real,x     
    )))
# z = np.random.normal(mu,1, size=n)
z = np.array(list(map(
  lambda z: (Base**z).imag,x       
    )))
# print('y',y)
# [print(Base**x1) for x1 in x]
print('x',x,'\n\ny',y,'\n\nz',z)


ax.scatter3D(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y (Re) ')
ax.set_zlabel('z (Im)')

plt.show()

# y = [(Base**x1) for x1 in x]


