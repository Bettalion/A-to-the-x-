from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Grab some test data.
X, Y, Z = axes3d.get_test_data(.1)

# X  = [1,2,3,4,5,6]
# Y = [1,2,3,4,5,6]
# Z = [1,2,3,4,5,6]

# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1)

plt.show()

print(axes3d.get_test_data(.1))