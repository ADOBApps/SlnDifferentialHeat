# _*_ coding: utf-8 _*_
"""
Created on 08/07/2022
	Functions to graph solution differential heat data
@author: ADOB

require matplotlib, sympy, numpy, scipy
execute: pip install matplotlib sympy numpy scipy

"""

import matplotlib.pyplot as plt
import numpy as np

# set params characteristics at all plots and subplots for implements latext
params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
plt.rcParams.update(params)

# Data
## General time data
time = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]

## H2O + KCl 0.50g
temp1 = [26.8, 26.8, 26.9, 26.9, 26.9, 26.9, 26.9, 26.9, 26.9, 26.9, 26.9]

## H2O + KCl 1.12g
temp2 = [26.0, 25.8, 25.7, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.6, 25.7]

## H2O + KCl 1.51g
temp3 = [25.3, 25.0, 24.8, 24.7, 24.6, 24.5, 24.5, 24.4, 24.4, 24.4, 24.4]

## H2O + KCl 2.0g
temp4 = [24.1, 23.5, 23.4, 23.3, 23.3, 23.2, 23.2, 23.2, 23.2, 23.2, 23.2]

## H2O + KCl 2.5g
temp5 = [22.9, 22.1, 21.9, 21.8, 21.8, 21.7, 21.7, 21.7, 21.8, 21.8, 21.8]

## H2O + KCl 3.0g
temp6 = [21.8, 21.0, 20.7, 20.7, 20.6, 20.6, 20.6, 20.6, 20.7, 20.7, 20.7]

# Create figure and axes
fig = plt.figure()
fig.clf()
ax = fig.add_subplot(1,1,1)

# Set title
ax.set_title(r'Curvas $H_{2}O + KCl$')

# Create the plot
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Temperatura (°C)")

ax.plot(time, temp1, label=r'$H_{2}O+0.50g KCl$')
ax.plot(time, temp1, 'bo')
ax.plot(time, temp2, label=r'$H_{2}O+1.12g KCl$')
ax.plot(time, temp2, 'bo')
ax.plot(time, temp3, label=r'$H_{2}O+1.51g KCl$')
ax.plot(time, temp3, 'bo')
ax.plot(time, temp4, label=r'$H_{2}O+2.00g KCl$')
ax.plot(time, temp4, 'bo')
ax.plot(time, temp5, label=r'$H_{2}O+2.50g KCl$')
ax.plot(time, temp5, 'bo')
ax.plot(time, temp6, label=r'$H_{2}O+3.00g KCl$')
ax.plot(time, temp6, 'bo')

# Show the major and minor grid lines
ax.grid(visible=True, which='major', color='#666666', linestyle='-')
ax.minorticks_on()
ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
## Legend
ax.legend(prop={'size': 6}, loc="upper right")

ax.plot(time, temp1, 'bo')
#plot([px], [py], 'bo')


# Save figure
fig.savefig("H2O+KCl-general.png")

# Show plot
plt.show()
