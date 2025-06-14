# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qslB_xp671zBNjvmq5K5Oc4vC2pLGmN5
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib as mlt
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns

#Contenido del dataset

#age: Edad del beneficiario
#sex: Sexo del contractor
#bmi: Indice de masa corporal, resultante del cociente entre el peso y la altura al cuadrado del individuo. Valores ideales: 18.5 to 24.9
#children: Cantidad de niños / Cantidad de dependientes
#smoker: Factor fumador
#region: Àrea residencial del beneficiario (USA): northeast, southeast, southwest, northwest.
#charges: Costo del seguro médico

# Cargar el .csv obtenido en el paso anterior
from google.colab import files
uploaded = files.upload()

# Cargamos el dataset en un dataframe
df_ins = pd.read_csv('insurance.csv')

df_ins

# EJERCICIO
# Calcular estadisticos basicos (media, mediana, desvio standard) de las columnas 'age', 'bmi' y 'charges' (TARGET)
# Hint: se puede utilizar metodos propios de los dataframes como .info o .describe, o aplicar metodos especificos

import pandas as pd

# Cargar el dataset (supongamos que ya tienes un DataFrame llamado df)
# df = pd.read_csv("archivo.csv")  # Solo si necesitas cargar un archivo

# Calcular estadísticos básicos usando métodos específicos
estadisticas = {
  "Media": df_ins[["age", "bmi", "charges"]].mean(),
  "Mediana": df_ins[["age", "bmi", "charges"]].median(),
  "Desvío estándar": df_ins[["age", "bmi", "charges"]].std()
}

# Mostrar los resultados
for clave, valores in estadisticas.items():
    print(f"{clave}:\n{valores}\n")

# Alternativamente, usando describe() para obtener varios estadísticos de una vez
print(df_ins[["age", "bmi", "charges"]].describe())

# Histograma de la variable target
fig, ax = plt.subplots(1, 1, figsize=(11,7))

sns.distplot(df_ins['charges'])

plt.show()

# EJERCICIO OPCIONAL
# Crear un pair plot con features seleccionadas y utilizar las configuraciones del grafico
# Hint: https://seaborn.pydata.org/generated/seaborn.pairplot.html

features_to_plot = ['###', '###', '###', '###'] # Atributos elegidos para el grafico

# Instanciamos pairplot
plot02 = sns.pairplot(df_ins[features_to_plot],
                      corner=True,
                      hue = 'sex'
                      )
plot02.map_lower(sns.kdeplot, levels=4, color=".2") # Definimos el tipo de grafico que queremos para auqellos por debajo de la diagona

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Cargar un dataset de ejemplo (puedes reemplazarlo con tu DataFrame real)
# df_ins = pd.read_csv("archivo.csv")  # Reemplaza con tu archivo

# Seleccionar las características a graficar
features_to_plot = ['age', 'bmi', 'charges', 'children', 'sex']  # Ajusta según tu dataset

# Crear el pairplot
plot02 = sns.pairplot(df_ins[features_to_plot],
                      corner=True,
                      hue='sex'  # Colorear según la variable 'sex'
                      )

# Agregar densidad de KDE en la parte inferior de la diagonal
plot02.map_lower(sns.kdeplot, levels=4, color=".2")

# Mostrar el gráfico
plt.show()

#Variables Dummies:
#En los casos en que se quiere entrenar un modelo de regresion lineal, debido a que el algoritmo procesa unicamente datos de tipo numerico, requiere que para los casos en donde el dataset contiene variables categoricas se le aplique un preprocesamiento
#Deben transformarse las variables categoricas en variables dummies, que son esencialmente una binarizacion de todas las opciones que hay para una variable categorica dada
#Por ej: en el caso de nuestro dataset tenemos la variable "smoker", que tiene dos valores posibles "yes"/"no". Para este caso se crean dos columnas nuevas en las que solo se toman valores 0/1, y se asigna un 1 para los casos en donde la columna dada es positiva para la etiqueta de la opcion de la que deriva:
#"smoker_yes"	"smoker_no"

# 1	0
# 1	0
# 1	0
# 0	1
# 1	0
# 0	1

#Nota: Para el caso de regresion lineal, por razones de multicolinealidad se elimina siempre una de estas columnas; es decir, si una variable categorica posee 5 valores unicos, las variables dummies derivadas seran 4 en total. Esta es una buena practica en general, incluso para modelos que no lo requieran, pero no es mandatoria en todos los casos (por ejemplo para randomforest)

# Se crean valores dummies para las variables categoricas del DataSet
df_cat = df_ins.select_dtypes(object) # Seleccion de las variables categoricas del dataset
df_cat = pd.get_dummies(df_cat, drop_first = True) # Creamos variables dummies

df_train_test = pd.concat([df_cat, df_ins.select_dtypes(np.number)], axis = 1)

X = df_train_test.drop(columns='charges')
y = df_train_test['charges']

#Implementacion modelo de regresion lineal

# EJERCICIO
# Importar las librerias necesarias para implementar una regresion lineal y un arbol de decision
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

df_train_test

# EJERCICIO
# Separar los datos en train y test (importar los modulos necesarios)
# Nota: utilizar el dataset con las variables dummies



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# Nota: cualquier cambio en el nombre de estas 4 variables debe ser modificado en la funcion de reporte mas abajo

import pandas as pd
from sklearn.model_selection import train_test_split

# Cargar el dataset con variables dummies (suponiendo que ya lo tienes)
# df = pd.read_csv("archivo.csv")

# Use df_train_test which contains the data with dummy variables
X = df_train_test.drop(columns=["charges"])
# Excluimos la columna objetivo
y = df_train_test["charges"]  # Variable objetivo

# Separar en conjuntos de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verificar tamaños de los conjuntos
print("Tamaño de X_train:", X_train.shape)
print("Tamaño de X_test:", X_test.shape)
print("Tamaño de y_train:", y_train.shape)
print("Tamaño de y_test:", y_test.shape)

# EJERCICIO
# Instanciar y entrenar el modelo (utilizando metodo .fit)

from sklearn.linear_model import LinearRegression

# Instanciar el modelo
modelo = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# Mostrar los coeficientes aprendidos
print("Coeficiente:", modelo.coef_)
print("Intercepto:", modelo.intercept_)

# EJERCICIO
# Realizar predicciones para el set de train y de test (utilizando metodo .predict)


# ¿Que tipo de objeto devuelve el .predict?, ¿como podria convertirse a dataFrame?

# Predicciones en el set de entrenamiento
y_train_pred = modelo.predict(X_train)

# Predicciones en el set de prueba
y_test_pred = modelo.predict(X_test)

# Mostrar algunos valores predichos
print("Predicciones en Train:", y_train_pred[:5])
print("Predicciones en Test:", y_test_pred[:5])

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Definimos una funcion para hacer un resumen de las metricas del modelo y generar una visualizacion de las predicciones y sus desvios:
def model_report(model, y_train_predicted, y_test_predicted, X_train = None, y_train = None, X_test = None, y_test = None):
    # Graficamos el modelo
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1) # Subplot for training data
    plt.scatter(y_train, y_train_predicted, alpha=0.5)
    plt.plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], 'k--', lw=2) # Diagonal line
    plt.xlabel("Valores reales (Train)")
    plt.ylabel("Predicciones (Train)")
    plt.title("Comparación Real vs. Predicciones (Entrenamiento)")

    plt.subplot(1, 2, 2) # Subplot for testing data
    plt.scatter(y_test, y_test_predicted, alpha=0.5)
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2) # Diagonal line
    plt.xlabel("Valores reales (Testeo)")
    plt.ylabel("Predicciones (Testeo)")
    plt.title("Comparación Real vs. Predicciones (Testeo)")

    plt.tight_layout()
    plt.show()

    print('MESTRICAS EN ENTRENAMIENTO: \n')
    print('Error cuadratico medio:             ', np.round(mean_squared_error(y_train, y_train_predicted), 3))
    print('Error absoluto medio:               ', np.round(mean_absolute_error(y_train, y_train_predicted), 3))
    print('Raiz del error cuadratico medio:    ', np.round(np.sqrt(mean_absolute_error(y_train, y_train_predicted)), 3))
    # Calculate R2 score for training data
    print('R2 Score:                           ', np.round(r2_score(y_train, y_train_predicted), 5))


    print('\n MESTRICAS EN TESTEO: \n')
    print('Error cuadratico medio:             ', np.round(mean_squared_error(y_test, y_test_predicted), 3))
    print('Error absoluto medio:               ', np.round(mean_absolute_error(y_test, y_test_predicted), 3))
    print('Raiz del error cuadratico medio:    ', np.round(np.sqrt(mean_absolute_error(y_test, y_test_predicted)), 3))
     # Calculate R2 score for testing data
    print('R2 Score:                           ', np.round(r2_score(y_test, y_test_predicted), 5))

import matplotlib.pyplot as plt

# Plotting for training data
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(y_train, y_train_pred, alpha=0.5)
plt.plot([y_train.min(), y_train.max()], [y_train.min(), y_train.max()], 'k--', lw=2)
plt.xlabel("Valores reales (Train)")
plt.ylabel("Predicciones (Train)")
plt.title("Comparación Real vs. Predicciones (Entrenamiento)")

# Plotting for testing data
plt.subplot(1, 2, 2)
plt.scatter(y_test, y_test_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)
plt.xlabel("Valores reales (Testeo)")
plt.ylabel("Predicciones (Testeo)")
plt.title("Comparación Real vs. Predicciones (Testeo)")

plt.tight_layout()
plt.show()

# Aplicamos el reporte al modelo de regresion lineal
model_report(model = model,
             y_train_predicted = y_train_pred,
             y_test_predicted = y_test_pred)

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def model_report_corrected(model, y_train_actual, y_train_predicted, y_test_actual, y_test_predicted):
    print("Evaluación del modelo:")

    # Errores en Train
    mse_train = mean_squared_error(y_train_actual, y_train_predicted)
    mae_train = mean_absolute_error(y_train_actual, y_train_predicted)
    r2_train = r2_score(y_train_actual, y_train_predicted)

    print(f"Train - MSE: {mse_train}, MAE: {mae_train}, R²: {r2_train}")

    # Errores en Test
    mse_test = mean_squared_error(y_test_actual, y_test_predicted)
    mae_test = mean_absolute_error(y_test_actual, y_test_predicted)
    r2_test = r2_score(y_test_actual, y_test_predicted)

    print(f"Test - MSE: {mse_test}, MAE: {mae_test}, R²: {r2_test}")

# Ahora ejecuta la función con los datos correctos
model_report_corrected(model, y_train, y_train_pred, y_test, y_test_pred)

# ¿Que otros atributos tiene la regresion lineal en sklearn?
# Hint: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Supongamos que ya tienes un DataFrame `df` con variables dummies
X = df.drop(columns=["charges"])  # Variables predictoras
y = df["charges"]  # Variable objetivo

# Dividir el dataset en train (80%) y test (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instanciar el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X_train, y_train)

# Coeficientes del modelo (impacto de cada variable en la predicción)
print("Coeficientes:", modelo.coef_)

# Intercepto (valor de 'charges' cuando todas las variables predictoras son 0)
print("Intercepto:", modelo.intercept_)

# Rango de la matriz X (importante para revisar problemas de colinealidad)
print("Rango de X:", modelo.rank_)

# Valores singulares de la matriz de entrada X
print("Valores singulares:", modelo.singular_)

# Número de características utilizadas durante el entrenamiento
print("Cantidad de features:", modelo.n_features_in_)

# Nombres de las características (si el DataFrame tiene nombres de columnas)
print("Nombres de features:", modelo.feature_names_in_)

# EJERCICIO OPCIONAL
# Implementar un arbol de decision e implementar otra regresion lineal aplicando estandarizacion a las variables

from sklearn.tree import DecisionTreeRegressor

# Instanciar el modelo de árbol de decisión
modelo_arbol = DecisionTreeRegressor(max_depth=4, random_state=42)

# Entrenar el modelo con los datos de entrenamiento
modelo_arbol.fit(X_train, y_train)

# Realizar predicciones
y_train_pred_arbol = modelo_arbol.predict(X_train)
y_test_pred_arbol = modelo_arbol.predict(X_test)

# Mostrar resultados básicos
print("Predicciones en Train (Árbol):", y_train_pred_arbol[:5])
print("Predicciones en Test (Árbol):", y_test_pred_arbol[:5])