# Librerías
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt

# CARGAR LA FECHA ACTUAL
fechaActual = dt.datetime.now()
# Formatear el objeto fecha actual para obtener la
# hora actual
horaActual = fechaActual.strftime('%H:%M')
horaCompar = dt.datetime.strptime(horaActual, '%H:%M').time()
# Día actual
diaSemActual = int(fechaActual.strftime('%w'))
diaSemActual -= 1       # Quitar 1

#%%
# Cargar la información de horarios del archivo de la base de datos
# Corresponde a una tabla
# Esto se realiza mediante la librería Pandas que trabaja perfectamente
# con archivos .csv
# En esta tabla, dado que hay valores vacíos (NaN) se eliminan, pues es
# complicado trabajar con ellos
horario = pd.read_csv('horarios24_2.csv', encoding='latin-1')
# Se puede rellenar con cualquier valor para que sea sencillo después trabajar
horario = horario.fillna('0')


#%%
# Obtener la lista de profesores ordenados alfabéticamente
# Se obtiene, leyendo de la tabla 'horario', la columna 'Profesor'
# luego a esto se le aplica el método unique() que regresa una columna de datos
# con valores únicos (sin repetición) y finalmente, se convierte en lista
profesores = horario['Profesor'].unique().tolist()

# TODO: Usando la lista profesores se puede rellenar un control para seleccionar
#       por ejemplo
print("--PROFESORES--")
print(profesores)

#%%
# Por ejemplo para obtener los grupos que lleva un profesor en particular
# Se usa de la tabla 'horario' se busca donde el valor de la columna 'Profesor' sea igual
# a algún valor
seleccion = horario[horario['Profesor'] == 'OLIVA MORENO LUZ NOE']
# Mostrar el horario del profesor seleccionado
print("--HORARIO--")
print(seleccion.to_string())

# TODO: Agregar una hora en específico para conocer disponibilidad de salón
# Revisar que salones están vacíos en la hora actual
# Generar una lista con los valores de los días de la semana en columnas
colSem = horario.columns[5:10].tolist()
# Recorrer todos los horarios
vac = []
for j, dd in enumerate(horario[colSem[int(diaSemActual)]]):
    # Si es diferente de cero
    if dd != '0':
        try:
            # Separar el tiempo en horas y minutos inicial y final de la clase
            ini, fin = dd.split('-')
            ini = dt.datetime.strptime(ini, '%H:%M').time()
            fin = dt.datetime.strptime(fin, '%H:%M').time()
            # Cuando el salón está ocupado
            if ini <= horaCompar <= fin:
                print('', end="")
            else:
                vac.append(j)
        except:
            print('', end="")
    # en otro caso
    else:
        vac.append(j)
# Mostrar los salones vacíos en esa hora
print("--SALONES VACÍOS--")
print( (horario.loc[vac, 'Salón'].unique().tolist()) )


# En otro caso, colocar un salón y buscar que horarios está ocupado
salon = horario[horario['Salón'] == '517']
print("--OCUPABILIDAD SALÓN--")
print(salon.to_string())
