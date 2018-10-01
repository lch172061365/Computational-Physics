import numpy
from numpy import random
a = random.random(size=(4,4))

matrixA = a
print(a)
m = []

for i in range(len(matrixA)):
    mnumber = max(matrixA[i])
    m.append(mnumber)
    pass

max_element = max(m)
print(max_element)
print("-"*60)

x,y = numpy.linalg.eig(a)
print("eigenvalue:",x)
print("-"*60)
print("eigenvector:",y)
