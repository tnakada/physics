#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 10:10:28 2018

@author: taikannakada
"""

import matplotlib.pyplot as plt
import numpy as np


totalMass= 5000 #kg
rocketMass=1000 #kg
burnoutTime=60 #kg
specificImpulse= 200 #kg
c=0.6 #drag constant
DT=0.01

numIterations= 40000
G=6.672 * 10**-11    
earthMass=5.972*10**24
earth_radius=6371000


dmdt=-(totalMass-rocketMass)/burnoutTime
thrust=c*specificImpulse*dmdt
   
 
time = 0
timeLst = [0]
    
mass= totalMass
massLst=[0]
    
position=0
positionLst=[0]
    
velocity=0
velocityLst=[0]

Density=1.225
DensityLst=[0]

drag_force=0
drag_forceLst=[0]

drag_acceleration=0
drag_accelerationLst=[0]

#Effective_force=0
#Effective_forceLst=[0]
   
gravitational_acceleration = -G*earthMass/(earth_radius**2)
gravitational_accelerationLst=[gravitational_acceleration]
    
thrust_acceleration=specificImpulse*dmdt*gravitational_acceleration/totalMass
thrust_accelerationLst=[thrust_acceleration]
    
acceleration=gravitational_acceleration+thrust_acceleration
accelerationLst=[acceleration]
    


for i in range (1,numIterations):
        time=i*DT
        timeLst.append(time)
 
        mass=mass+dmdt*DT
        massLst.append(mass)
        if (mass<=1000):
            dmdt=0
        
        
        
        Density=1.225*np.exp(-0.1385*position)
        DensityLst.append(Density)
       
        
        gravitational_acceleration=-G*earthMass/(earth_radius+position)**2
        gravitational_accelerationLst.append(gravitational_acceleration)
        
        thrust_acceleration=specificImpulse*dmdt*gravitational_acceleration/mass
        thrust_accelerationLst.append(thrust_acceleration)
        
        drag_force = 0.5*c*Density*4*np.pi*np.absolute(velocity)
        drag_forceLst.append(drag_force)
        
        drag_acceleration=-drag_force/mass
        drag_accelerationLst.append(drag_acceleration)
        
        #Effective_force = thrust - drag_force
        #Effective_forceLst.append(Effective_force)
        
        acceleration=gravitational_acceleration+thrust_acceleration+drag_acceleration
        accelerationLst.append(acceleration)
        
        velocity=velocity+acceleration*DT
        velocityLst.append(velocity)
        
        position=position+velocity*DT
        positionLst.append(position)

plt.plot(timeLst, velocityLst, label='velocity')
plt.figure()
plt.plot(timeLst, positionLst, label='position')
