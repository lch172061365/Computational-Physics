import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.image as img

G = 6.67*10**(-11)

m1 = 6*10**24 #earth
m2 = 2*10**30 #sun
m3 = 1.9*10**27 #jupiter

#m1
x10 = -149597870000
y10 = 0
z10 = 0
p10 = 0
q10 = 29783
r10 = 0
#m2
x20 = 0
y20 = 0
z20 = 0
p20 = 0
q20 = 0
r20 = 0
#m3
x30 = 778547200000
y30 = 0
z30 = 0
p30 = 0
q30 = -13070
r30 = 0


dt = 2000 
n = 1000000 

#initialize the position
x1 = [0]
y1 = [0]
z1 = [0]

x2 = [0]
y2 = [0]
z2 = [0]

x3 = [0]
y3 = [0]
z3 = [0]

x1[0] = x10 #set up initial position
y1[0] = y10
z1[0] = z10

x2[0] = x20
y2[0] = y20
z2[0] = z20

x3[0] = x30
y3[0] = y30
z3[0] = z30

#initialzie the speed, create a list
p1 = [0]
q1 = [0]
r1 = [0]

p2 = [0]
q2 = [0]
r2 = [0]

p3 = [0]
q3 = [0]
r3 = [0]

p1[0] = p10 #set up initial speed
q1[0] = q10
r1[0] = r10

p2[0] = p20
q2[0] = q20
r2[0] = r20

p3[0] = p30
q3[0] = q30
r3[0] = r30

#loop
i = 0
while i < n-1:
    #three distances
    S12 = math.sqrt((x2[i]-x1[i])**2+(y2[i]-y1[i])**2+(z2[i]-z1[i])**2)
    S13 = math.sqrt((x3[i]-x1[i])**2+(y3[i]-y1[i])**2+(z3[i]-z1[i])**2)
    S23 = math.sqrt((x2[i]-x3[i])**2+(y2[i]-y3[i])**2+(z2[i]-z3[i])**2)


    x1.append(x1[i]+p1[i]*dt)
    y1.append(y1[i]+q1[i]*dt)
    z1.append(z1[i]+r1[i]*dt)
    x2.append(x2[i]+p2[i]*dt)
    y2.append(y2[i]+q2[i]*dt)
    z2.append(z2[i]+r2[i]*dt)
    x3.append(x3[i]+p3[i]*dt)
    y3.append(y3[i]+q3[i]*dt)
    z3.append(z3[i]+r3[i]*dt)

    p1.append(dt*(G*m3*(x3[i+1]-x1[i+1])/((S13)**3)+G*m2*(x2[i+1]-x1[i+1])/((S12)**3))+p1[i])
    q1.append(dt*(G*m3*(y3[i+1]-y1[i+1])/((S13)**3)+G*m2*(y2[i+1]-y1[i+1])/((S12)**3))+q1[i])
    r1.append(dt*(G*m3*(z3[i+1]-z1[i+1])/((S13)**3)+G*m2*(z2[i+1]-z1[i+1])/((S12)**3))+r1[i])
    p2.append(dt*(G*m1*(x1[i+1]-x2[i+1])/((S12)**3)+G*m3*(x3[i+1]-x2[i+1])/((S23)**3))+p2[i])
    q2.append(dt*(G*m1*(y1[i+1]-y2[i+1])/((S12)**3)+G*m3*(y3[i+1]-y2[i+1])/((S23)**3))+q2[i])
    r2.append(dt*(G*m1*(z1[i+1]-z2[i+1])/((S12)**3)+G*m3*(z3[i+1]-z2[i+1])/((S23)**3))+r2[i])
    p3.append(dt*(G*m1*(x1[i+1]-x3[i+1])/((S13)**3)+G*m2*(x2[i+1]-x3[i+1])/((S23)**3))+p3[i])
    q3.append(dt*(G*m1*(y1[i+1]-y3[i+1])/((S13)**3)+G*m2*(y2[i+1]-y3[i+1])/((S23)**3))+q3[i])
    r3.append(dt*(G*m1*(z1[i+1]-z3[i+1])/((S13)**3)+G*m2*(z2[i+1]-z3[i+1])/((S23)**3))+r3[i])

    #next loop
    i += 1

import mpl_toolkits.mplot3d.axes3d as p3

#make plot
def update_lines(num,datalines,lines):
    for line,data in zip(lines,datalines):
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines
fig = plt.figure()
ax = p3.Axes3D(fig)

#data turple
data=[np.array([x1,y1,z1])[:,0:1000000:100],
      np.array([x2,y2,z2])[:,0:1000000:100],
      np.array([x3,y3,z3])[:,0:1000000:100]]

lines =[ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]

#make plot
ax.set_xlim3d([-10**12,10**12])
ax.set_xlabel('X')
ax.set_ylim3d([-10**12,10**12])
ax.set_ylabel('Y')
ax.set_zlim3d([-10**12,10**12])
ax.set_zlabel('Z')
ax.set_title('Simulation on three-body')

#figure show
line_ani = animation.FuncAnimation(fig, update_lines,fargs = (data,lines),interval =1,blit = False)
plt.show()
