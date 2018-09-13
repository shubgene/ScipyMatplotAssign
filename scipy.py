    # -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:51:44 2018

@author: shurastogi
"""



#1. fitting it to the periodic function
#2. plot the fit

import scipy as sc
import numpy as np
import matplotlib.pyplot as plt

Max = np.array([39, 41, 43, 47, 49, 51, 45, 38, 37, 29, 27, 25])
Min = np.array([21, 23, 27, 28, 32, 35, 31, 28, 21, 19, 17, 18])
months=np.arange(12)
days = np.linspace(0, 12, num=365)

from scipy import optimize
def periodic_func(times, avg, ampl, time_offset):
    return (avg
            + ampl * np.cos((times + time_offset) * 2 * np.pi / times.max()))

res_max, cov_max = optimize.curve_fit(periodic_func, months,
                                      Max,[20, 10, 0])
res_min, cov_min = optimize.curve_fit(periodic_func, months,
                                      Min,[-40, 20, 0])

plt.plot(months,Max,'ro')
plt.plot(days, periodic_func(days, *res_max), 'r-')
plt.plot(months,Min,'bo')
plt.plot(days, periodic_func(days, *res_min), 'b-')
plt.xlabel('month')
plt.ylabel('Temperature($^\circ$C)')