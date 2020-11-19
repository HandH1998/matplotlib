import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 0.1 * x

plt.figure()
plt.plot(x, y, lw=10,zorder=1)

plt.ylim((-2, 2))
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 绑定xaxis和yaxis对应的是哪个spine
# 因为默认的xaxis和yaxis对应的是bottom和left
# 所以这里其实是可以不写下面两行的
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# xaxis绑定到yaxis的对应位置
ax.spines['bottom'].set_position(('data', 0))
# yaxis绑定到xaxis的对应位置
ax.spines['left'].set_position(('data', 0))

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))
    # 前置图形的zorder值要比plot的zorder值大才能显示出来
    label.set_zorder(2)
plt.show()
