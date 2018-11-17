import time
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

def init_state(N):   
    ''' generates a random spin configuration for initial condition'''
    # np.random.randint(2, size=(N,N)) generate random number and return as a list
    state = 2*np.random.randint(2, size=(N,N))-1
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

nt      = 16        # samples number
N       = 40       # lattice number L
eqSteps = 2**10       # equilibrium step
mcSteps = 2**10       # monte carlo step
 
Energy = [] # E
Magnetization  = [] # M
SpecificHeat = []  # Cv
Susceptibility = [] # K
 
T= np.linspace(2.0,2.3,nt)
T =list(T)
 
n1 = 1/mcSteps*N*N
n2 = 1/mcSteps**2*N*N

time_start=time.time()
j = 0
for t in T:
    E = 0 
    M = 0 
    cv = 0 
    k = 0 
    config = init_state(N)
    # reach equilibrium
    for i in range(eqSteps):
        flipping(config, 1/t)
    # sample caculate
    for i in range(mcSteps):
        flipping(config, 1/t)
        e = calculate_energy(config)
        m= calculate_magnetic(config)
        E += e
        M += m
        cv += e*e
        k += m*m
    Cv = (n1*cv - n2*E*E)/(t*t)
    K = (n1*k - n2*M*M)/t
    Energy.append(E*n1)
    Magnetization.append(M*n1)
    SpecificHeat.append(Cv)
    Susceptibility.append(K/(mcSteps**2*N*N))
    j +=1
    if j%10==0:
        print("Step number %d completed" %j)
time_end=time.time()
print('totally cost',time_end-time_start)

Magnetization = np.array(Magnetization)
 
f = plt.figure(figsize=(18, 10)); # plot the calculated values    
 
sp =  f.add_subplot(2, 2, 1 )
plt.plot(T, Energy, 'o', color="red")
plt.xlabel("Temperature (T)", fontsize=20)
plt.ylabel("Energy ", fontsize=20)
 
sp =  f.add_subplot(2, 2, 2 )
plt.plot(T, abs(Magnetization), 'o', color="blue")
plt.xlabel("Temperature (T)", fontsize=20)
plt.ylabel("Magnetization ", fontsize=20)
 
sp =  f.add_subplot(2, 2, 3 )
plt.plot(T, SpecificHeat, 'o', color="red")
plt.xlabel("Temperature (T)", fontsize=20)
plt.ylabel("Specific Heat ", fontsize=20)
 
sp =  f.add_subplot(2, 2, 4 )
plt.plot(T, Susceptibility, 'o', color="blue")
plt.xlabel("Temperature (T)", fontsize=20)
plt.ylabel("Susceptibility", fontsize=20)

plt.show()
