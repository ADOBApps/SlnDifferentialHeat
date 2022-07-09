# _*_ coding: utf-8 _*_
"""
Created on 08/07/2022
	Functions to graph solution differential heat data
@author: ADOB

require matplotlib, sympy, numpy, scipy
execute: pip install matplotlib sympy numpy scipy
"""

from Mycontrollers.math.linearmath import LinearSolve
from Myviews.saltgraph import Salt

mysalt = Salt()
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

if __name__ == "__main__":
	mysalt.Comparison("H2O+KCl-general.png", time, temp1, temp2, temp3, temp4, temp5, temp6)

	## H2O + KCl 0.50g
	mysalt.Any(r'Curvas $H_{2}O + KCl$', "Tiempo (s)", "Temperatura (°C)", "H2O+KCl_0.50.png", time, temp1, r'$H_{2}O+0.50g KCl$')

	## H2O + KCl 1.12g
	mysalt.Any(r'Curvas $H_{2}O + KCl$', "Tiempo (s)", "Temperatura (°C)", "H2O+KCl_1.12.png", time, temp2, r'$H_{2}O+1.12g KCl$')

	## H2O + KCl 1.51g
	mysalt.Any(r'Curvas $H_{2}O + KCl$', "Tiempo (s)", "Temperatura (°C)", "H2O+KCl_1.51.png", time, temp3, r'$H_{2}O+1.51g KCl$')

	## H2O + KCl 2.0g
	mysalt.Any(r'Curvas $H_{2}O + KCl$', "Tiempo (s)", "Temperatura (°C)", "H2O+KCl_2.00.png", time, temp4, r'$H_{2}O+2.00g KCl$')

	## H2O + KCl 2.5g
	mysalt.Any(r'Curvas $H_{2}O + KCl$', "Tiempo (s)", "Temperatura (°C)", "H2O+KCl_2.50.png", time, temp5, r'$H_{2}O+2.50g KCl$')

	## H2O + KCl 3.0g
	mysalt.Any(r'Curvas $H_{2}O + KCl$', "Tiempo (s)", "Temperatura (°C)", "H2O+KCl_3.00.png", time, temp6, r'$H_{2}O+3.00g KCl$')

	## H2O + KCl 0.50g
	LinearSolve(time, temp1, r'Distribución $H_{2}O+KCl(0.50g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_0.50.png")

	## H2O + KCl 1.12g
	LinearSolve(time, temp2, r'Distribución $H_{2}O+KCl(1.12g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_1.12.png")

	## H2O + KCl 1.51g
	LinearSolve(time, temp3, r'Distribución $H_{2}O+KCl(1.51g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_1.51.png")

	## H2O + KCl 2.0g
	LinearSolve(time, temp4, r'Distribución $H_{2}O+KCl(2.00g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_2.00.png")

	## H2O + KCl 2.5g
	LinearSolve(time, temp5, r'Distribución $H_{2}O+KCl(2.50g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_2.50.png")

	## H2O + KCl 3.0g
	LinearSolve(time, temp6, r'Distribución $H_{2}O+KCl(3.00g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_3.00.png")

	