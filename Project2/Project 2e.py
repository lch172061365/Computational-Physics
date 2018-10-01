import numpy as np
import time

n = int(input('choose n for matrix:'))
a1 = np.eye(n,k=0)
a2 = np.eye(n,k=1)
a3 = np.eye(n,k=-1)

w = 0.5
p = input()
y = input()
x = input()+(w*p)**2+1/p
z = input()

a = x*a1+y*a2+z*a3
matrixA = a

m = len(matrixA)
i = 0


while i < n-1:
    x = matrixA[i][i]
    y = matrixA[i+1][i]
    mtp= y/x
    matrixA[i+1] = matrixA[i+1] - mtp*matrixA[i]
    i = i+1
    pass

print(matrixA)
