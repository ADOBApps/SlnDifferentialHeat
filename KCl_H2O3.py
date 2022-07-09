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

## H2O + KCl 1.51g
temp3 = [25.3, 25.0, 24.8, 24.7, 24.6, 24.5, 24.5, 24.4, 24.4, 24.4, 24.4]

# Create figure and axes
fig = plt.figure()
fig.clf()
ax = fig.add_subplot(1,1,1)

# Set title
ax.set_title(r'Curvas $H_{2}O + KCl$')

# Create the plot
ax.set_xlabel("Tiempo (s)")
ax.set_ylabel("Temperatura (°C)")
ax.plot(time, temp3, label=r'$H_{2}O+1.51g KCl$')
ax.plot(time, temp3, 'bo')


# Show the major and minor grid lines
ax.grid(visible=True, which='major', color='#666666', linestyle='-')
ax.minorticks_on()
ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
## Legend
ax.legend(prop={'size': 10}, loc="upper right")


# Save figure
fig.savefig("H2O+KCl_1.51.png")

# Show plot
plt.show()
