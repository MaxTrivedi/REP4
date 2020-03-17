#!/usr/bin/env python
import math as mt
import matplotlib.pyplot as plt
import numpy as np

#Units for width and height can be thought as being in millimetres
w = 1*1000
l = 1*1000
print('Enter diameter as a fraction of width(e.g: 0.1):')
user_input = float(input())
r1 = int(user_input*1000/2)
r2 = 0

x=mt.pi/6

placements = []

#Initialise figure for plotting
plt.figure(num=None, figsize=(5, 5), dpi=175, facecolor='w', edgecolor='k')
axes = plt.gca()
axes.set_xlim([0,w])
axes.set_ylim([0,l])
plt.xticks([], [])
plt.yticks([], [])
plt.xlabel('Width = 1m, Radii = '+str(r1)+'m')
plt.ylabel('Length = 1m')

#Locations for every other circle 
for j in np.arange(r1,l-r1,4*r1*mt.cos(x)):
    for i in range(int(w//(2*r1))):
        placements.append([(2*i+1)*r1,j])

for j in np.arange(r1+2*mt.cos(x)*r1,l-r1,4*r1*mt.cos(x)):
    for i in range(int(w//(2*r1))-1):
        placements.append([(2*i+1)*r1+r1*2*mt.sin(x),j])

#Plotting circles
for placement in placements:
    axes.add_artist(plt.Circle((placement[0],placement[1]),r1,fill=False))

print(len(placements), 'circles plotted.')

plt.show()



'''
#initial placement
while True:     
    for j in range(l):
        for i in range(w):
            if i >= r1 and j >= r1:
                placements.append([i,j])
                axes.add_artist(plt.Circle((i,j),r1))
                break
        if len(placements)>0:
            break
    break 
print(placements)
#plt.show()



for j in range(l):
    for i in range(w):
            if math.sqrt((placements[0][0] - i)**2+(placements[0][1] - j)**2)> 2*r1:
                print(i,j)
                axes.add_artist(plt.Circle((i,j),r1))
plt.show()     
'''




