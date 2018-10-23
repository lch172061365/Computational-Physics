import matplotlib.pyplot as plt
import numpy as np
import math

G = 6.67*10**(-11)

m1 = 6*10**24 #just a random mass for escape planet
m2 = 2*10**30 #sun

#m1
x10 = 1.5*10**11 #1 AU

#we have that equation: (mv^2)/2=(β-1)GMm/r^(β-1), and v is the escape velocity
beta = list(range(200,300,1))
esc_v = []
for i in range(0,100,1):
    beta[i] = beta[i]/100
    v = math.sqrt(2*G*m2*(beta[i]-1)/(x10**(beta[i]-1)))
    esc_v.append(v)
    pass

x_values = beta
y_values = esc_v
plt.figure('beta-escape velocity')
ax = plt.gca()
ax.set_xlabel('beta')
ax.set_ylabel('escape velocity')
ax.plot(x_values, y_values, color='r', linewidth=1, alpha=0.6)

plt.show()
