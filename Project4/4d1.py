import time
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
from collections import Counter

N       = 20       # lattice number L
eqSteps = 2**10       # equilibrium steps
mcSteps = 2**10       # monte carlo step
t = 1.0 #temperature
Energy = [] # E
n1 = 1/mcSteps*N*N
n2 = 1/mcSteps**2*N*N


def init_state(N):   
    ''' generates a random spin configuration for initial condition'''
    # np.random.randint(2, size=(N,N)) generate random number and return as a list
    state = 2*np.random.randint(2, size=(N,N))-1
    return state


def flipping(grid, beta):
    '''Monte Carlo move using Metropolis algorithm '''
    transfer = grid.copy()
    N = len(grid)
    for i in range(N):
        for j in range(N):
                # generate random number from 0 to N-1
                a = np.random.randint(0, N)
                b = np.random.randint(0, N)
                s = transfer[a][b]
                E = transfer[(a+1)%N][b] + transfer[a][(b+1)%N] + transfer[(a-1)%N][b] + transfer[a][(b-1)%N]
                cost = 2*s*E
                # if the energy fall down, then s flip
                if cost < 0:
                    s *= -1
                # generate random number from 0 to 1, if P < exp(-E/(kT)), then flip
                elif rand() < np.exp(-cost*beta):
                    s *= -1
                transfer[a][b] = s
    return transfer

def calculate_energy(grid):
    '''Energy of a given configuration'''
    energy = 0
    N = len(grid)
    for i in range(N):
        for j in range(N):
            S = grid[i][j]
            E = grid[(i+1)%N][j] + grid[i][(j+1)%N] + grid[(i-1)%N][j] + grid[i][(j-1)%N]
                energy += -E*S
    # the closest four points
    return energy/4

def probability():
    grid = init_state(N)
    x1 = grid
    beta = 1/t
    n = 0
    k = True
    while k:
        y1 = flipping(x1,beta)
        if (y1 == x1).all() == True:
            k = False
            e = calculate_energy(y1)
            return e
        else:
            n+=1
            x1 = y1

i = 0
number = 10 # samples numbers, which is the total number for distribution
while i < number:
    ei = probability()
    Energy.append(ei)
    i += 1

print(Energy)

count = Counter(Energy)
d = dict(count)

d1=sorted(d.items(),key=lambda x:x[0])
print(d1)

keys = [x[0] for x in d1]
values = [x[1]/number for x in d1]

plt.figure('P(E) distribution')
ax = plt.gca()
ax.set_xlabel('Energy')
ax.set_ylabel('Probability')


xticks = np.arange(1, len(keys)+1)
bar_width=0.5
ax.bar(xticks, values, width=bar_width, edgecolor='none')
ax.set_xticks(xticks)
ax.set_xticklabels(keys)
ax.set_xlim(0,len(xticks))

plt.show()


