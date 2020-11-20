import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig, ax = plt.subplots()

x = np.arange(0, 2 * np.pi, 0.01)
line, = ax.plot(x, np.sin(x))

# 定义每一帧的函数
def animate(i):
    line.set_ydata(np.sin(x + i / 10))
    return line


def init():
    line.set_ydata(np.sin(x))
    return line


# func:如何变化的函数  frames:总共帧数  init_func:起始时间的函数  interval:相邻两帧间隔时间
ani = animation.FuncAnimation(fig=fig, func=animate, frames=100,
                              init_func=init, interval=20, blit=False)
plt.show()
