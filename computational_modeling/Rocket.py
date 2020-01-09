#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:18:13 2018

@author: taikannakada,
         gordanhua,
         silviawang,
         jacquelinezhu,
         sawyerharris
"""

import matplotlib.pyplot as plt

totalMass= 5000 #kg
rocketMass=1000 #kg
burnoutTime=60 #kg
specificImpulse= 200 #kg
DT=0.01

numIterations= 40000
G=6.672 * 10**-11    
earthMass=5.972*10**24
earth_radius=6371000

dmdt=-(totalMass-rocketMass)/burnoutTime
    
time = 0
timeLst = [0]
    
mass= totalMass
massLst=[0]
    
position=0
positionLst=[0]
    
velocity=0
velocityLst=[0]
    
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
        
        position=position+velocity*DT
        positionLst.append(position)
        
        gravitational_acceleration=-G*earthMass/(earth_radius+position)**2
        gravitational_accelerationLst.append(gravitational_acceleration)
        
        thrust_acceleration=specificImpulse*dmdt*gravitational_acceleration/mass
        thrust_accelerationLst.append(thrust_acceleration)
        
        
        acceleration=gravitational_acceleration+thrust_acceleration
        accelerationLst.append(acceleration)
        
        velocity=velocity+acceleration*DT
        velocityLst.append(velocity)
    

plt.plot(timeLst, velocityLst, label='velocity')
plt.figure()
plt.plot(timeLst, positionLst, label='position')