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


# Show the major and minor grid lines
ax.grid(visible=True, which='major', color='#666666', linestyle='-')
ax.minorticks_on()
ax.grid(visible=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
## Legend
ax.legend(prop={'size': 10}, loc="lower right")


# Save figure
fig.savefig("H2O+KCl_0.50.png")

# Show plot
plt.show()
