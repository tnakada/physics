#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  8 22:37:57 2018

@author: taikannakada

Model of the population of cyanobacteria in a petri dish under simulated day-night environments.

"""

import numpy as np
import matplotlib.pyplot as plt


initial_population = 1 #initial population of cyanobacteria
carrying_capacity = 1000000 #carrying capacity of cyanobacteria
birth_rate_day = 1 #rate of birth when cyanobacteria is exposed to daylight
final_time = 40 #hours
dt = 0.001 #hours
time = np.arange(0, final_time + dt, dt) #in hours (finalTime + dt is used so finalTime is inclusive)
population = np.zeros(time.size)

#the initial population is given to the first index of the population array.

population[0] = initial_population

for t in np.arange(1, time.size):
    
    if (time[t] % 24 >= 12):
        #At these times, there is no light, so the birth rate is 0.
        birth_rate = 0
    else:
        #Otherwise, the birth rate is the set to the daytime birth rate.
        birth_rate = birth_rate_day
    #population at time time[t] based on the population at time time[t-1].
    population[t] = population[t - 1] + birth_rate * population[t - 1] * (1 - (population[t - 1] / carrying_capacity)) * dt

#create and label plot, then save plot as pdf 
plt.plot(time, population)
plt.title('Cyanobacteria Population Over Time', weight = 'bold')
plt.xlabel('Time (hours)')
plt.ylabel('Population')
plt.grid(True)
plt.savefig("bacteriaPlot.pdf")
