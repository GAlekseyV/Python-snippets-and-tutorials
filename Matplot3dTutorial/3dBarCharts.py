from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

xpos = [x for x in range(1, 11)]
ypos = [x for x in range(1, 11)]
zpos = [x*0 for x in range(0, 10)]

dx = np.ones(10)
dy = np.ones(10)
dz = [x for x in range(1, 11)]

ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
plt.show()
