import time
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

N       = 20       # lattice number L
eqSteps = 2**10       # equilibrium steps
mcSteps = 2**10       # monte carlo step
t = 1 #temperature

def init_state(N):   
    ''' generates a random spin configuration for initial condition'''
    # np.random.randint(2, size=(N,N)) generate random number and return as a list
    state = [[1]*N]*N
    print("-"*60)
    print("start figure for Ising model(direction represented by +1 or -1):")
    print()
    print(state)
    print()
    print("-"*60)
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
                # if the energy fall down, then flip
                if cost < 0:
                    s *= -1
                # generate random number from 0 to 1, if P < exp(-E/(kT)), then flip
                elif rand() < np.exp(-cost*beta):
                    s *= -1
                transfer[a][b] = s
    return transfer

grid = init_state(N)
x1 = grid
beta = 1/t
n = 0
k = True
while k:
    y1 = flipping(x1,beta)
    if y1 == x1:
        print("-"*60)
        print("end figure for Ising model(direction represented by +1 or -1):")
        print()
        print(y1)
        print()
        print("-"*60)
        print(n)
        
        k = False
    else:
        n+=1
        x1 = y1







