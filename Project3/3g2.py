import matplotlib.pyplot as plt
import numpy as np
import math

G = 6.67*10**(-11)

m1 = 3.3*10**23 #mercury
m2 = 2*10**30 #sun

AU = 1.5*10**11
yr = 365*24*3600

#m1
x10 = 0.3075*AU
y10 = 0
z10 = 0
p10 = 0
q10 = 12.44*AU/yr
r10 = 0
#m2
x20 = 0
y20 = 0
z20 = 0
p20 = 0
q20 = 0
r20 = 0

#simulation elements
dt = 360 #dt，one loop for 0.1h
n = 10*24*365*10 #one century

#initialize the position, create the list for position
x1 = [0]
y1 = [0]
z1 = [0]

x2 = [0]
y2 = [0]
z2 = [0]

x1[0] = x10 #set the initial position
y1[0] = y10
z1[0] = z10

x2[0] = x20
y2[0] = y20
z2[0] = z20


#initialize the speed, create the list for speed
p1 = [0]
q1 = [0]
r1 = [0]

p2 = [0]
q2 = [0]
r2 = [0]

p1[0] = p10 #set the initial speed
q1[0] = q10
r1[0] = r10

p2[0] = p20
q2[0] = q20
r2[0] = r20

tan_angle = [0]
time = [0]
#loop
i = 0
while i < n-1:
    #distance between sun and mercury
    S12 = math.sqrt((x2[i]-x1[i])**2+(y2[i]-y1[i])**2+(z2[i]-z1[i])**2)


    #regard the movement of the earth as a uniform linear motion 
    x1.append(x1[i]+p1[i]*dt)
    y1.append(y1[i]+q1[i]*dt)
    z1.append(z1[i]+r1[i]*dt)
    x2.append(x2[i]+p2[i]*dt)
    y2.append(y2[i]+q2[i]*dt)
    z2.append(z2[i]+r2[i]*dt)

    radius = x1[i]**2+y1[i]**2
    radius_after = x1[i+1]**2+y1[i+1]**2
    radius_before =x1[i-1]**2+y1[i-1]**2

    if radius < radius_after and radius <radius_before:#judge perihelion
        tan_angle.append(y1[i]/x1[i])
        time.append(dt*i/(3600*24*365))
    else:
        pass
    
    #at the end of t, the velocity will increase a*t, but now we have a phase for relativity
    #which is 1+3*(p1[i]**2+q1[i]**2)/(6*10**18)
    p1.append(dt*((1+3*(p1[i]**2+q1[i]**2)/(6*10**18))*G*m2*(x2[i+1]-x1[i+1])/((S12)**3))+p1[i])
    q1.append(dt*((1+3*(p1[i]**2+q1[i]**2)/(6*10**18))*G*m2*(y2[i+1]-y1[i+1])/((S12)**3))+q1[i])
    r1.append(dt*((1+3*(p1[i]**2+q1[i]**2)/(6*10**18))*G*m2*(z2[i+1]-z1[i+1])/((S12)**3))+r1[i])
    p2.append(dt*((1+3*(p2[i]**2+q2[i]**2)/(6*10**18))*G*m1*(x1[i+1]-x2[i+1])/((S12)**3))+p2[i])
    q2.append(dt*((1+3*(p2[i]**2+q2[i]**2)/(6*10**18))*G*m1*(y1[i+1]-y2[i+1])/((S12)**3))+q2[i])
    r2.append(dt*((1+3*(p2[i]**2+q2[i]**2)/(6*10**18))*G*m1*(z1[i+1]-z2[i+1])/((S12)**3))+r2[i])
    
    #next loop
    i += 1

x_values = time
y_values = tan_angle
print(tan_angle)
plt.figure('tan_perihelion and time')
ax = plt.gca()
ax.set_xlabel('year')
ax.set_ylabel('tan_perihelion')
ax.plot(x_values, y_values, color='r', linewidth=1, alpha=0.6)
plt.show()

