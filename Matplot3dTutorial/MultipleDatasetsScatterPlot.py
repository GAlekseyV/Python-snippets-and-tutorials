from mpl_toolkits.mplot3d import axes3d
import  matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = [range(0, 11)]
Y = [range(0, 11)]
Z = [x**2 for x in range(0, 11)]

Xs = [range(0, 11)]
Ys = [range(0, 11)]
Zs = [x**3 for x in range(0, 11)]

ax.scatter(X, Y, Z, c='r', marker='o')
ax.scatter(Xs, Ys, Zs, c='b', marker='^')
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')

plt.show()
