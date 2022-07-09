# Tratamiento de datos
# ==============================================================================
import pandas as pd
import numpy as np

# Gráficos
# ==============================================================================
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

# Preprocesado y modelado
# ==============================================================================
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import statsmodels.api as sm
import statsmodels.formula.api as smf
# Configuración warnings
# ==============================================================================
import warnings
warnings.filterwarnings('ignore')

class LinearSolve:

	def __init__ (self, xs, ys, title, xlabel, ylabel, figname):
		print("Calling constructor")

		bateos = xs
		runs = ys
		
		datos = pd.DataFrame({'bateos': bateos, 'runs': runs})
		datos.head(3)

		# Gráfico
		# ==============================================================================
		# set params characteristics at all plots and subplots for implements latext
		params = {'text.latex.preamble': [r'\usepackage{siunitx}', r'\usepackage{amsmath}']}
		plt.rcParams.update(params)

		fig, ax = plt.subplots(2, 1,figsize=(6, 3.84), sharex=True, sharey=True)

		# Set the title for the figure
		fig.suptitle("Linealización", fontsize=15)

		datos.plot(
			x = 'bateos',
			y = 'runs',
			c = 'firebrick',
			kind = "scatter",
			ax = ax[0]
		)
		ax[0].set_title(title);
		ax[0].set_xlabel(xlabel)
		ax[0].set_ylabel(ylabel)

		# Correlación lineal entre las dos variables
		# ==============================================================================
		corr_test = pearsonr(x = datos['bateos'], y =  datos['runs'])
		print("Coeficiente de correlación de Pearson: ", corr_test[0])
		print("P-value: ", corr_test[1])

		# División de los datos en train y test
		# ==============================================================================
		X = datos[['bateos']]
		y = datos['runs']

		X_train, X_test, y_train, y_test = train_test_split(
			X.values.reshape(-1,1),
			y.values.reshape(-1,1),
			train_size   = 0.8,
			random_state = 1234,
			shuffle      = True
		)

		# Creación del modelo
		# ==============================================================================
		modelo = LinearRegression()
		modelo.fit(X = X_train.reshape(-1, 1), y = y_train)

		# Información del modelo
		# ==============================================================================
		print("Intercept:", modelo.intercept_)
		print("Coeficiente:", list(zip(X.columns, modelo.coef_.flatten(), )))
		print("Coeficiente de determinación R^2:", modelo.score(X, y))

		# Error de test del modelo 
		# ==============================================================================
		predicciones = modelo.predict(X = X_test)
		print(predicciones[0:3,])

		rmse = mean_squared_error(
			y_true  = y_test,
			y_pred  = predicciones,
			squared = False
		)
		print("")
		print(f"El error (rmse) de test es: {rmse}")

		# División de los datos en train y test
		# ==============================================================================
		X = datos[['bateos']]
		y = datos['runs']

		X_train, X_test, y_train, y_test = train_test_split(
			X.values.reshape(-1,1),
			y.values.reshape(-1,1),
			train_size   = 0.8,
			random_state = 1234,
			shuffle      = True
		)
		# Creación del modelo utilizando matrices como en scikitlearn
		# ==============================================================================
		# A la matriz de predictores se le tiene que añadir una columna de 1s para el intercept del modelo
		X_train = sm.add_constant(X_train, prepend=True)
		modelo = sm.OLS(endog=y_train, exog=X_train,)
		modelo = modelo.fit()
		print(modelo.summary())

		# Intervalos de confianza para los coeficientes del modelo
		# ==============================================================================
		modelo.conf_int(alpha=0.05)

		# Predicciones con intervalo de confianza del 95%
		# ==============================================================================
		predicciones = modelo.get_prediction(exog = X_train).summary_frame(alpha=0.05)
		predicciones.head(4)

		# Predicciones con intervalo de confianza del 95%
		# ==============================================================================
		predicciones = modelo.get_prediction(exog = X_train).summary_frame(alpha=0.05)
		predicciones['x'] = X_train[:, 1]
		predicciones['y'] = y_train
		predicciones = predicciones.sort_values('x')

		# Gráfico del modelo
		# ==============================================================================
		#fig, ax = plt.subplots(figsize=(6, 3.84))
		
		ax[1].set_title(f"{title} Linealizada");
		ax[1].set_xlabel(xlabel)
		ax[1].set_ylabel(ylabel)

		ax[1].scatter(predicciones['x'], predicciones['y'], marker='o', color = "gray")
		ax[1].plot(predicciones['x'], predicciones["mean"], linestyle='-', label="OLS")
		ax[1].plot(predicciones['x'], predicciones["mean_ci_lower"], linestyle='--', color='red', label="95% CI")
		ax[1].plot(predicciones['x'], predicciones["mean_ci_upper"], linestyle='--', color='red')
		ax[1].fill_between(predicciones['x'], predicciones["mean_ci_lower"], predicciones["mean_ci_upper"], alpha=0.1)
		ax[1].legend();

		plt.savefig(figname)
		plt.show()

		# Error de test del modelo 
		# ==============================================================================
		X_test = sm.add_constant(X_test, prepend=True)
		predicciones = modelo.predict(exog = X_test)
		rmse = mean_squared_error(
			y_true  = y_test,
			y_pred  = predicciones,
			squared = False
			)
		print("")
		print(f"El error (rmse) de test es: {rmse}")

	def __del__ (self):
		class_name = self.__class__.__name__
		print(class_name, "destroyed")


time = [0, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300]

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

## H2O + KCl 0.50g
LinearSolve(time, temp1, r'Distribución $H_{2}O+KCl(0.50g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_0.50.png")

## H2O + KCl 1.12g
#LinearSolve(time, temp2, r'Distribución $H_{2}O+KCl(1.12g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_1.12.png")

## H2O + KCl 1.51g
#LinearSolve(time, temp3, r'Distribución $H_{2}O+KCl(1.51g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_1.51.png")

## H2O + KCl 2.0g
#LinearSolve(time, temp4, r'Distribución $H_{2}O+KCl(2.00g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_2.00.png")

## H2O + KCl 2.5g
#LinearSolve(time, temp5, r'Distribución $H_{2}O+KCl(2.50g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_2.50.png")

## H2O + KCl 3.0g
#LinearSolve(time, temp6, r'Distribución $H_{2}O+KCl(3.00g)$', "Tiempo (s)", "Temperatura(°C)", "linealizacion_3.00.png")


#(self, xs, ys, title, xlabel, ylabel, figname)