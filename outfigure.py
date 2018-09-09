import matplotlib.pyplot as plt
import math
import numpy as np

x = [10,100,1000,10000]
y = [0.00001, 0.0009996891021728516,0.006010532379150391,0.32295680046081543]

for i in range(0,4):
    x[i] = math.log10(x[i])
    y[i] = math.log10(y[i])
    pass
z1 = np.polyfit(x,y,1)
p1 = np.poly1d(z1)
print(z1)
print(p1)
plt.figure('time-n fig')
ax = plt.gca()
ax.set_xlabel('lg(n)')
ax.set_ylabel('lg(time)')

ax.plot(x,y)
plt.show()
    
    
