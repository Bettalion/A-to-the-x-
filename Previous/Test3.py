import matplotlib.pyplot as plt
import numpy as np

x= np.array(range(-10,10))
y= np.array(range(-10,10))
# Compute z to make the pringle surface.
z = np.sin(-x*y)

ax = plt.figure().add_subplot(projection='3d')

ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)

plt.show()