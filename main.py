# _*_ coding: utf-8 _*_
"""
Created on 08/07/2022
	Functions to graph solution differential heat data
@author: ADOB

require matplotlib, sympy, numpy, scipy
execute: pip install matplotlib sympy numpy scipy
"""

from Mycontrollers.math.linearmath import LinearSolveComp
from Mycontrollers.math.linearmath import LinearSolve
from Myviews.saltgraph import Salt

mysalt = Salt()
# Data TvsT
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

# Data Heat solution vs n (moles)
n_B = [0.0067, 0.0217, 0.0420, 0.0688, 0.1023, 0.1426]
slnH = [-93.32, 279.9, 559.9, 839.8, 1026.5, 279.9]

# Data Heat integral solution vs molality
molality = [0.1397, 0.4526, 0.8745, 1.4333, 2.1318, 2.970]
intHeat = [-13.9137, 18.6344, 27.6431, 31.3051, 30.6101, 6.9568]

# Plot graph and linearRegression type Time vs Temperature
def MakeTvsT():
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
	LinearSolveComp(time, temp1, r'Distribución $H_{2}O+KCl(0.50g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_0.50.png", 6)
	## H2O + KCl 1.12g
	LinearSolveComp(time, temp2, r'Distribución $H_{2}O+KCl(1.12g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_1.12.png", 6)
	## H2O + KCl 1.51g
	LinearSolveComp(time, temp3, r'Distribución $H_{2}O+KCl(1.51g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_1.51.png", 6)
	## H2O + KCl 2.0g
	LinearSolveComp(time, temp4, r'Distribución $H_{2}O+KCl(2.00g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_2.00.png", 6)
	## H2O + KCl 2.5g
	LinearSolveComp(time, temp5, r'Distribución $H_{2}O+KCl(2.50g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_2.50.png", 6)
	## H2O + KCl 3.0g
	LinearSolveComp(time, temp6, r'Distribución $H_{2}O+KCl(3.00g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_3.00.png", 6)

# Plot Heat solution vs n (moles)
def MakeSlnHvsn():
	#
	mysalt.Any(
		r'Curvas $H_{2}O + KCl$', 
		r'$n_{B} (moles)$', 
		r'$\Delta{H_{S}}(J)$', 
		"SlnHvsn.png", 
		n_B, 
		slnH, 
		r'$H_{2}O+KCl$'
		)
	LinearSolve(
		n_B, 
		slnH, 
		r'Distribución $\Delta{H_{S}}$ vs $n_{B}$', 
		r'$n_{B} (moles)$', 
		r'$\Delta{H_{S}}(J)$', 
		"linealizacion_slnHvsn.png",
		9
		)

# Plot Heat integral solution vs molality
def MakeIntHvsm():
	#
	mysalt.Any(
		r'Curvas $H_{2}O + KCl$', 
		r'$molalidad$', 
		r'$\Delta{H_{Int, B}}(\frac{KJ}{mol})$', 
		"IntHvsm.png", 
		molality, 
		intHeat, 
		r'$H_{2}O+KCl$'
		)
	LinearSolve(
		molality, 
		intHeat, 
		r'Distribución $\Delta{H_{Int, B}}$ vs $molalidad$', 
		r'$molalidad$', 
		r'$\Delta{H_{Int, B}}(\frac{KJ}{mol})$', 
		"linealizacion_IntHvsm.png",
		9
		)

if __name__ == "__main__":
	#MakeSlnHvsn()
	MakeIntHvsm()
	