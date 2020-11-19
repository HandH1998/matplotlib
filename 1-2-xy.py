import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2 + 1

# figsize设置figure的大小，num是figure的顺序
plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

# limit x y label range  注意参数是一个元组
plt.xlim((-1, 2))
plt.ylim((-2, 3))
# set x y label
plt.xlabel('I am x')
plt.ylabel('I am y')
# set new x y 标尺
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
print(type(new_ticks))
plt.xticks(new_ticks)
# 这里可以输入类似latex的行内数学公式位于两个$之间，但是与正则表达式类似，有两重解析，可以使用原始字符串
plt.yticks([-2, -1.8, -1, 1.22, 3], [r'$really\ bad$', r'$bad\alpha$', r'$normal$', r'$good$', r'$really\ good$'])

# gca='get current axis'
# 下面是为了可以自定义axis的位置
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 绑定xaxis和yaxis对应的是哪个spine
# 因为默认的xaxis和yaxis对应的是bottom和left
# 所以这里其实是可以不写下面两行的
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
# xaxis绑定到yaxis的对应位置
ax.spines['bottom'].set_position(('data',-1))
# yaxis绑定到xaxis的对应位置
ax.spines['left'].set_position(('data',-1))

plt.show()
