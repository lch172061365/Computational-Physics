import numpy as np
X = [1/20,1/40,1/60,1/80,1/100]
Y = [2.23,2.23,2.24,2.26,2.26]
z1 = np.polyfit(X, Y, 1)  
p1 = np.poly1d(z1)
print(z1) 
print(p1) 



