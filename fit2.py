import matplotlib.pyplot as plt
import numpy as np
X = [60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
Y = [132,136,141,145,150,155,160,165,170,175,180,185,190,195,201,206,212,218,223,229,234]
z1 = np.polyfit(X, Y, 1)  #一次多项式拟合，相当于线性拟合
p1 = np.poly1d(z1)
print(z1)  
print(p1)
plt.plot(X,Y,1)
plt.show()
