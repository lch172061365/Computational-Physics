import numpy as np
import time

n = int(input('choose n for matrix:'))
a1 = np.eye(n,k=0)
a2 = np.eye(n,k=1)
a3 = np.eye(n,k=-1)
e = input()
d = input()
p = input()

a = (d+p**2)*a1+e*a2+e*a3
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
