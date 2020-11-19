import matplotlib.pyplot as plt
import numpy as np

n = 12
x = np.arange(n)
y1 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)  # uniform均匀分布
y2 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(x, +y1, facecolor='#9999ff', edgecolor='white')
plt.bar(x, -y2, facecolor='#ff9999', edgecolor='white')

for x1, y in zip(x, y1):
    # ha:horizontal alignment va:vertical alignment   这里的对齐是以确定的点 按照center bottom对齐，类似css里的方式
    plt.text(x1, y + 0.05, '%.2f' % y, ha='center', va='bottom')

for x1, y in zip(x, y2):
    plt.text(x1, -y - 0.05, '-%.2f' % y, ha='center', va='top')

plt.xlim(-0.5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())
plt.show()
