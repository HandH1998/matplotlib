import matplotlib.pyplot as plt
import numpy as np

n=1024
x=np.random.normal(0,1,n)
y=np.random.normal(0,1,n)
t=np.arctan2(y,x) #arctan2(y,x)=arctan(y/x) #[-pi,pi] for color value

plt.scatter(x,y,s=75,c=t,alpha=0.5)
# plt.scatter(np.arange(5),np.arange(5))
plt.xlim((-5,5))
plt.ylim((-5,5))

# delete x y 标尺
plt.xticks(())
plt.yticks(())

plt.show()
