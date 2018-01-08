#!/usr/bin/env python

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from laspy.file import File
import sys


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect('equal')

# plot data
ground = File(sys.argv[1], mode='r')
max_points = int(sys.argv[2])
points = ground.X.size
step = int(points / max_points)
points = ax.plot(ground.X[::step], ground.Y[::step], ground.Z[::step], '.')

# bounding box for equal aspect ratio
max_range = 0.5 * \
    np.array([ground.X.ptp(), ground.Y.ptp(), ground.Z.ptp()]).max()
mid_x = 0.5 * (ground.X.min() + ground.X.max())
mid_y = 0.5 * (ground.Y.min() + ground.Y.max())
mid_z = 0.5 * (ground.Z.min() + ground.Z.max())
ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

plt.show()
