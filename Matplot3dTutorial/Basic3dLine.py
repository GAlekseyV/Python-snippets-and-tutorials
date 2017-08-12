from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X, Y, Z = [range(0, 10)], [range(0, 10)], [x**2 for x in range(0, 10)]
ax.plot_wireframe(X, Y, Z)

plt.show()