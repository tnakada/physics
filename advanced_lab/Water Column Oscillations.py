#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 18:47:38 2019

@author: taikannakada
"""

'''
Curve Fitting in Python

To export the data to Python, right click on the data and choose 
Copy Data -> Full Presicion. Paste into Excel (as an intermediate step). 
The first two rows are tites.

Then open Spyder and run teh following Python script by copying it into the 
"editor pane" on the left and clicking the green "Run" arrow 

'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

print('Your x data and y data should appear as columns in Excel\n')
input('Copy your x data to clipboard and press Enter')

x = pd.read_clipboard(header=None)
x = np.array(x).T[0]
input('Copy your y data to clipboard and press Enter')

y = pd.read_clipboard(header=None)
y = np.array(y).T[0]

def function(t,a,b,c,d):
    return a * np.exp(-b*t) * np.cos(c*t+d)

popt, pcov = curve_fit(function, x, y)

plt.plot(x, y, 'o')

yfit = function(x, *popt)

plt.plot(x, yfit)

perr = np.sqrt(np.diag(pcov))
r2 = r2_score(y, yfit)

print('The fitting parameters are ', popt)
print('The uncertainties int he fitting parameters are ', perr)
print('The coefficient of determination is ', r2)

'''
the fit gives you the best estimate of the observed frequency. (The angular 
frequency is the third fitting parameter, c, in the Python script above.) 
Compare with your theoretical expression. Alter the aount of water int he tube. 
Repeat
'''
