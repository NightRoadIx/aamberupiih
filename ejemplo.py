# Librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
from datetime import datetime

#%%
# Cargar la información del horario del archivo de la base de datos
# Corresponde a una tabla
# Esto se realiza mediante la librería Pandas que trabaja perfectamente
# con archivos .csv
# En esata tabla, dado que hay valores vacíos (NaN) se eliminan, pues es
# complicado trabajar con ellos
horario = pd.read_csv('mecaHorario.csv')
# Se puede rellenar con cualquier valor para que sea sencillo después trabajar
horario = horario.fillna('0')
# Cargar la información de los grupos
grupos = pd.read_csv('mecaGrupos.csv')

# Mostrar la tabla con los datos de horario por ejemplo
print(horario)

#%%
# Obtener la lista de profesores ordenados alfabéticamente
# Se obtiene, leyendo de la tabla 'horario', la columna 'Profesor'
# luego a esto se le aplica el método unique() que regresa una columna de datos
# con valores únicos (sin repetición) y finalmente, se convierte en lista
profesores = horario['Profesor'].unique().tolist()

# TODO: Usando la lista profesores se puede rellenar un control para seleccionar
#       por ejemplo
print(profesores)

#%%
# Por ejemplo para obtener los grupos que lleva un profesor en particular
# Se usa de la tabla 'horario' se busca donde el valor de la columna 'Profesor' sea igual
# a algún valor
seleccion = horario[horario['Profesor'] == 'HERNANDEZ QUINTANAR LUIS FELIPE DE JESUS']

# Mostrar el horario del profesor seleccionado
print(seleccion.to_string())
# TODO: Con esto es posible revisar ya una hora específica para saber ubicación

# La hora actual del sistema se puede obtener mediante:
# Lista con los días de la semana tal como vienen en la tabla
setimana = horario.columns[5:11].tolist()
# Obtiene una fotografía de la fecha y hora
now = datetime.now()
# Obtener la fecha y hora en una cadena con formato
horaStr = now.strftime("%H:%M")
diaSem = setimana[int(now.strftime("%w"))]
print(f"Hoy es {diaSem} a las {horaStr}")
# TODO: A partir de eso se compara con el intervalo que viene en las columnas de horario

#%%
# Obtener la lista de los grupos que tenga el profesor
grup = seleccion['Grupo'].unique().tolist()
# Obtener las materias que da el profesor
mater = seleccion['Asignatura'].unique().tolist()

#%%
# Ahora con los grupos determinar cuántos alumnos tiene en total
totalAlumnos = 0
for gr, ma in zip(grup, mater):
    # Obtener los datos de la materia
    lab = grupos[ grupos['Nombre de la Materia'] == ma ]
    for i in lab.index:
        totalAlumnos += lab['Inscritos'][i]

print("Grupos: ", grup)
print("Materias: ", mater)
print("Total de alumnos: ", totalAlumnos)