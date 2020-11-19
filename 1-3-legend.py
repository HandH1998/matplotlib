import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2 + 1

# figsize设置figure的大小，num是figure的顺序
plt.figure(num=3, figsize=(8, 5))

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

# 添加图例需要先在plot里加上参数label
# 然后legend
# 或者直接在legend中加参数labels
# plt.plot(x, y2,label='up')
# plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--',label='down')

# l1和l2是返回的line对象，这样就可以在legend中使用handles，自定义选择要不要给这条线加图例
# 但是注意plt.plot返回的是元组，因此接收时用l1,  l2,
l1,=plt.plot(x, y2,label='up')
l2,=plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--',label='down')
plt.legend(handles=[l1,l2],labels=['aa','bbb'],loc='best')

plt.show()
