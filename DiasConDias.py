import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('DATAGRAFICO.csv')

# Filtrar las filas correspondientes al día "lunes"
df_lunes = df[df['Dia'] == 'Lunes']

print(df_lunes['Mochilas'])
mochilas_semana1 = []
personas_semana1 = []
for fila in df_lunes:
    if fila['semana1 '] == '':
        mochilas_semana1.append(fila['Mochilas'])
        personas_semana1.append(fila['Personas'])
print(mochilas_semana1)
print(personas_semana1)