import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)  # 添加3d axis

X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)

R = np.sqrt(X ** 2+Y ** 2)
# height value
Z = np.sin(R)
# rstride cstride 行跨和列跨
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
# zdir:从哪个方向投影  offset：得到的等高线图的位置
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow')

plt.show()
