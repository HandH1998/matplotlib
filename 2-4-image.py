import matplotlib.pyplot as plt
import numpy as np

#image data
a=np.random.uniform(0,1,9).reshape(3,3)

# interpolation 插值方法
plt.imshow(a,interpolation='nearest',cmap='bone',origin='upper')
plt.colorbar(shrink=0.9)

plt.xticks(())
plt.yticks(())
plt.show()