import matplotlib.pyplot as plt
import numpy as np


def f(x, y):
    # the height function
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)


n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)

X, Y = np.meshgrid(x, y)  # 网格化
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)  # cmap:colormap  8：等高线把全图分成8部分
C = plt.contour(X, Y, f(X, Y), 8, colors='blue', linewidth=0.5)  # 生成等高线
plt.clabel(C, inline=True, fontsize=10)  # 加标注

plt.xticks(())
plt.yticks(())
plt.show()
