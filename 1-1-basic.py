import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2 + 1

plt.figure()
plt.plot(x, y1)

# figsize设置figure的大小，num是figure的顺序
plt.figure(num=3, figsize=(8, 5))
plt.plot(x, y2)
# color，linewidth，linestyle
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
plt.show()
