import random
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import itertools
import pylab

x = [1,2,3,4,5]
y = [5,4,3,2,1]
z = [1,2,3,4,0]

# plt.plot(x,y,z)
# plt.show()


fig = pylab.figure()
ax = Axes3D(fig)
ax.plot_surface(x,y,z , rstride=1, cstride=1)
pylab.show()
