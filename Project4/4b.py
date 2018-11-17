import time
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

N       = 20       # lattice number L
eqSteps = 2**10       # equilibrium step
mcSteps = 2**10       # monte carlo step

def init_state(N):   
    ''' generates a random spin configuration for initial condition'''
    # np.random.randint(2, size=(N,N)) generate random number and return as a list
    state = 2*np.random.randint(2, size=(N,N))-1
    print("-"*60)
    print("start figure for Ising model(direction represented by +1 or -1):")
    print()
    print(state)
    print()
    print("-"*60)
    return state


def flipping(grid, beta):
    '''Monte Carlo move using Metropolis algorithm '''
    N = len(grid)
    for i in range(N):
        for j in range(N):
                # generate random number from 0 to N-1
                a = np.random.randint(0, N)
                b = np.random.randint(0, N)
                s = grid[a][b]
                E = grid[(a+1)%N][b] + grid[a][(b+1)%N] + grid[(a-1)%N][b] + grid[a][(b-1)%N]
                cost = 2*s*E
                # if the energy fall down, then turn around
                if cost < 0:
                    s *= -1
                # generate random number from 0 to 1, if P < exp(-E/(kT)), then turn around
                elif rand() < np.exp(-cost*beta):
                    s *= -1
                grid[a][b] = s
    print("-"*60)
    print("end figure for Ising model(direction represented by +1 or -1):")
    print()
    print(grid)
    print()
    print("-"*60)
    return grid

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

def calculate_magnetic(grid):
    '''Magnetization of a given configuration'''
    mag = np.sum(grid)
    return mag

Energy = [] # E
Magnetization  = [] # M
SpecificHeat = []  # Cv
Susceptibility = [] # K
t = 1
n1 = 1/mcSteps*N*N
n2 = 1/mcSteps**2*N*N

def element():
    config = init_state(N)
    flipping(config,1/t)
    e = calculate_energy(config)
    m= calculate_magnetic(config)

    cv = e*e
    k = m*m

    Cv = (n1*cv - n2*e*e)/(t*t)
    K = (n1*k - n2*m*m)/t
    print("the results are as follows:")
    print()
    print("E:",e)
    print("M:",m)
    print("Cv:",Cv)
    print("K:",K)

if __name__ == '__main__':
    element()

