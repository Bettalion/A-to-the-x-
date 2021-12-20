import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D 

import numpy as np
fig = plt.figure()
np.random.seed(31)

mu = 3
n = 50 
# x = np.random.normal(mu,1, size=n)
# print(x.shape)
x = np.array(list(range(n)))
print(x.shape)
y = np.random.normal(mu,1, size=n)
z = np.random.normal(mu,1, size=n)

plt.rcParams['figure.figsize']=(8,5)

ax = Axes3D(fig)

ax.scatter3D(x,y,z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()



# print(ax)


# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization! 

# fig = plt.figure()
# ax = Axes3D(fig) #<-- Note the difference from your original code...

# X, Y, Z = axes3d.get_test_data(0.05)
# cset = ax.contour(X, Y, Z, 16, extend3d=True)
# ax.clabel(cset, fontsize=9, inline=1)
# plt.show()