import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2 * x + 1
plt.plot(x, y)

plt.figure(num=1, figsize=(8, 5))
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

# 引出一条线
x0 = 1
y0 = 2 * x0 + 1
plt.scatter(x0, y0, s=50, color='b')
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)  # black 虚线

# method 1
# xy 标注的点坐标 xycoords 标注的点基于的坐标系
# xytext 标注的文字的坐标  textcoords  标注的文字的坐标即xytext基于的坐标系
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30), textcoords='offset points'
             , fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

# method 2
plt.text(-3.7,3,r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',fontdict={'size':16,'color':'b'})
plt.show()
