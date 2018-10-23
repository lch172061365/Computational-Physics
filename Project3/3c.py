import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.image as img

G = 6.67*10**(-11)

m1 = 6*10**24 #earth
m2 = 2*10**30 #sun

#m1
x10 = 149597870000
y10 = 0
z10 = 0
p10 = 0
q10 = -29783
r10 = 0
#m2
x20 = 0
y20 = 0
z20 = 0
p20 = 0
q20 = 0
r20 = 0

#simulation elements
dt = 500#dt，one loop for 500 seconds
n = 200000 #the number of loop
day = 500/(24*3600) #the number of the days

daylist=[0]
daylist[0] = day
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


#loop
i = 0
while i < n-1:
    #distance between sun and earth
    S12 = math.sqrt((x2[i]-x1[i])**2+(y2[i]-y1[i])**2+(z2[i]-z1[i])**2)

    #the time schedule
    day += 500/(24*3600)
    daylist.append(day)


    #regard the movement of the earth as a uniform linear motion 
    x1.append(x1[i]+p1[i]*dt)
    y1.append(y1[i]+q1[i]*dt)
    z1.append(z1[i]+r1[i]*dt)
    x2.append(x2[i]+p2[i]*dt)
    y2.append(y2[i]+q2[i]*dt)
    z2.append(z2[i]+r2[i]*dt)

    #at the end of t, the velocity will increase a*t
    p1.append(dt*(G*m2*(x2[i+1]-x1[i+1])/((S12)**3))+p1[i])
    q1.append(dt*(G*m2*(y2[i+1]-y1[i+1])/((S12)**3))+q1[i])
    r1.append(dt*(G*m2*(z2[i+1]-z1[i+1])/((S12)**3))+r1[i])
    p2.append(dt*(G*m1*(x1[i+1]-x2[i+1])/((S12)**3))+p2[i])
    q2.append(dt*(G*m1*(y1[i+1]-y2[i+1])/((S12)**3))+q2[i])
    r2.append(dt*(G*m1*(z1[i+1]-z2[i+1])/((S12)**3))+r2[i])

    #next loop
    i += 1

#make plot, x for blue and y for orange
d_values = daylist
x_values = x1
y_values = y1

plt.scatter(d_values,x_values,s=1)
plt.scatter(d_values,y_values,s=1)

plt.title("earth-sun data",fontsize=24)
plt.xlabel("day",fontsize=14)
plt.ylabel("positon",fontsize=14)

plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()

