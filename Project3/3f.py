import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.image as img

G = 6.67*10**(-11)


m1 = 2*10**30 #sun
m2 = 3.3*10**23 #mercury
m3 = 4.9*10**24#venus
m4 = 6*10**24#earth
m5 = 6.6*10**23#mars
m6 = 1.9*10**27#jupiter
m7 = 5.5*10**26#saturn
m8 = 8.8*10**25#uranus
m9 = 1.03*10**26#neptun

#m1 position and speed 
x10 = 0
y10 = 0
z10 = 0
p10 = 0
q10 = 0
r10 = 0
#m2
x20 = 57409050000
y20 = 0
z20 = 0
p20 = 0
q20 = 48053
r20 = 0
#m3
x30 = 108208930000
y30 = 0
z30 = 0
p30 = 0
q30 = 35030
r30 = 0
#m4
x40 = 149597870000
y40 = 0
z40 = 0
p40 = 0
q40 = 30000
r40 = 0
#m5
x50 = 227939100000
y50 = 0
z50 = 0
p50 = 0
q50 = 24130
r50 = 0
#m6
x60 = 778330000000
y60 = 0
z60 = 0
p60 = 0
q60 = 13060
r60 = 0
#m7
x70 = 1427000000000
y70 = 0
z70 = 0
p70 = 0
q70 = 9640 
r70 = 0
#m8
x80 = 2869000000000
y80 = 0
z80 = 0
p80 = 0
q80 = 6810
r80 = 0
#m9
x90 = 4504000000
y90 = 0
z90 = 0
p90 = 0
q90 = 5430
r90 = 0

#loop elements
dt = 10000 #dt
n = 1000000 #number of loop

#initialize the position and create the list 
x1 = [0]
y1 = [0]
z1 = [0]*n

x2 = [0]
y2 = [0]
z2 = [0]*n

x3 = [0]
y3 = [0]
z3 = [0]*n

x4 = [0]
y4 = [0]
z4 = [0]*n

x5 = [0]
y5 = [0]
z5 = [0]*n

x6 = [0]
y6 = [0]
z6 = [0]*n

x7 = [0]
y7 = [0]
z7 = [0]*n

x8 = [0]
y8 = [0]
z8 = [0]*n

x9 = [0]
y9 = [0]
z9 = [0]*n

x1[0] = x10 #set the initial position
y1[0] = y10
z1[0] = z10

x2[0] = x20
y2[0] = y20
z2[0] = z20

x3[0] = x30
y3[0] = y30
z3[0] = z30

x4[0] = x40
y4[0] = y40
z4[0] = z40

x5[0] = x50
y5[0] = y50
z5[0] = z50

x6[0] = x60
y6[0] = y60
z6[0] = z60

x7[0] = x70
y7[0] = y70
z7[0] = z70

x8[0] = x80
y8[0] = y80
z8[0] = z80

x9[0] = x90
y9[0] = y90
z9[0] = z90


#initialize the speed and create the list for sped
p1 = [0]
q1 = [0]
r1 = [0]

p2 = [0]
q2 = [0]
r2 = [0]

p3 = [0]
q3 = [0]
r3 = [0]

p4 = [0]
q4 = [0]
r4 = [0]

p5 = [0]
q5 = [0]
r5 = [0]

p6 = [0]
q6 = [0]
r6 = [0]

p7 = [0]
q7 = [0]
r7 = [0]

p8 = [0]
q8 = [0]
r8 = [0]

p9 = [0]
q9 = [0]
r9 = [0]

p1[0] = p10 #set initial speed
q1[0] = q10
r1[0] = r10

p2[0] = p20
q2[0] = q20
r2[0] = r20

p3[0] = p30
q3[0] = q30
r3[0] = r30

p4[0] = p40
q4[0] = q40
r4[0] = r40

p5[0] = p50
q5[0] = q50
r5[0] = r50

p6[0] = p60
q6[0] = q60
r6[0] = r60

p7[0] = p70
q7[0] = q70
r7[0] = r70

p8[0] = p80
q8[0] = q80
r8[0] = r80

p9[0] = p90
q9[0] = q90
r9[0] = r90

#fix the sun, cause the mass of sun is so large that we can regard it as a fixed point
x1 = [0]*n
y1 = [0]*n
p1 = [0]*n
q1 = [0]*n


#main loop
i = 0
while i < n-1:
    #distance
    S12 = x20
    S13 = x30
    S14 = x40
    S15 = x50
    S16 = x60
    S17 = x70
    S18 = x80
    S19 = x90

    #same as the code before
    x2.append(x2[i]+p2[i]*dt)
    y2.append(y2[i]+q2[i]*dt)

    x3.append(x3[i]+p3[i]*dt)
    y3.append(y3[i]+q3[i]*dt)

    x4.append(x4[i]+p4[i]*dt)
    y4.append(y4[i]+q4[i]*dt)

    x5.append(x5[i]+p5[i]*dt)
    y5.append(y5[i]+q5[i]*dt)

    x6.append(x6[i]+p6[i]*dt)
    y6.append(y6[i]+q6[i]*dt)

    x7.append(x7[i]+p7[i]*dt)
    y7.append(y7[i]+q7[i]*dt)
    
    x8.append(x8[i]+p8[i]*dt)
    y8.append(y8[i]+q8[i]*dt)
    
    x9.append(x9[i]+p9[i]*dt)
    y9.append(y9[i]+q9[i]*dt)

    #same as the code before, only more planets
    p2.append(dt*(G*m1*(x1[i+1]-x2[i+1])/((S12)**3))+p2[i])
    q2.append(dt*(G*m1*(y1[i+1]-y2[i+1])/((S12)**3))+q2[i])

    p3.append(dt*(G*m1*(x1[i+1]-x3[i+1])/((S13)**3))+p3[i])
    q3.append(dt*(G*m1*(y1[i+1]-y3[i+1])/((S13)**3))+q3[i])

    p4.append(dt*(G*m1*(x1[i+1]-x4[i+1])/((S14)**3))+p4[i])
    q4.append(dt*(G*m1*(y1[i+1]-y4[i+1])/((S14)**3))+q4[i])

    p5.append(dt*(G*m1*(x1[i+1]-x5[i+1])/((S15)**3))+p5[i])
    q5.append(dt*(G*m1*(y1[i+1]-y5[i+1])/((S15)**3))+q5[i])

    p6.append(dt*(G*m1*(x1[i+1]-x6[i+1])/((S16)**3))+p6[i])
    q6.append(dt*(G*m1*(y1[i+1]-y6[i+1])/((S16)**3))+q6[i])

    p7.append(dt*(G*m1*(x1[i+1]-x7[i+1])/((S17)**3))+p7[i])
    q7.append(dt*(G*m1*(y1[i+1]-y7[i+1])/((S17)**3))+q7[i])

    p8.append(dt*(G*m1*(x1[i+1]-x8[i+1])/((S18)**3))+p8[i])
    q8.append(dt*(G*m1*(y1[i+1]-y8[i+1])/((S18)**3))+q8[i])

    p9.append(dt*(G*m1*(x1[i+1]-x9[i+1])/((S19)**3))+p9[i])
    q9.append(dt*(G*m1*(y1[i+1]-y9[i+1])/((S19)**3))+q9[i])


    #next loop
    i += 1

#the data is so large, it will be very slow to show the figure    
fig = plt.figure()
ax = Axes3D(fig)
ax = fig.gca(projection = '3d')
ax.plot(x1,y1,z1)
ax2 = fig.gca(projection = '3d')
ax2.plot(x2,y2,z2)
ax3 = fig.gca(projection = '3d')
ax3.plot(x3,y3,z3)
ax4 = fig.gca(projection = '3d')
ax4.plot(x4,y4,z4)
ax5 = fig.gca(projection = '3d')
ax5.plot(x5,y5,z5)
ax6 = fig.gca(projection = '3d')
ax6.plot(x6,y6,z6)
ax7 = fig.gca(projection = '3d')
ax7.plot(x7,y7,z7)
ax8 = fig.gca(projection = '3d')
ax8.plot(x8,y8,z8)
ax9 = fig.gca(projection = '3d')
ax9.plot(x9,y9,z9)
plt.show()
