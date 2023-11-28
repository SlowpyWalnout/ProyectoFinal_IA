import csv
import matplotlib.pyplot as plt

# Definir los arrays
hora = []
mochilas = []
personas = []

# Leer el archivo CSV
with open('DATAGRAFICO-5semanas.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Iterar sobre las filas del archivo
    for row in reader:
        # Agregar los datos a los arrays
        hora.append(row['Hora'])
        mochilas.append(int(row['Mochilas']))
        personas.append(int(row['Personas']))

def dividir_lista(lista, tamano):
    return [lista[i:i+tamano] for i in range(0, len(lista), tamano)]

# Definir el tamaño deseado (84 elementos)
tamano_sublista = 84

# Dividir las listas
hora_dividida = ['02:30', '02:35', '02:40', '02:45', '02:50', '02:55', '03:00', '04:30', '04:35', '04:40', '04:45', '04:50', '04:55', '05:00', '06:30', '06:35', '06:40', '06:45', '06:50', '06:55', '07:00']
mochilas_divididas = dividir_lista(mochilas, tamano_sublista)
personas_divididas = dividir_lista(personas, tamano_sublista)

# Crear la nueva lista que simula ser la original pero dividida
lista_dividida = list(zip(mochilas_divididas, personas_divididas))    
semana1 = lista_dividida[0]
semana2 = lista_dividida[1]
semana3 = lista_dividida[2]
semana4 = lista_dividida[3]
semana5 = lista_dividida[4]

print(len(semana1))

mochilas_semana1 = semana1[0]
personas_semana1 = semana1[1]

mochilas_semana2 = semana2[0]
personas_semana2 = semana2[1]

mochilas_semana3 = semana3[0]
personas_semana3 = semana3[1]

mochilas_semana4 = semana4[0]
personas_semana4 = semana4[1]

mochilas_semana5 = semana5[0]
personas_semana5 = semana5[1]

print(hora_dividida)
print(mochilas_semana4)
print(personas_semana4)
#=======================================================================
#semana1-semana2
#=======================================================================
fig, ax = plt.subplots()
ax.scatter(mochilas_semana1, personas_semana1, color='blue', label='Semana 1')
ax.scatter(mochilas_semana2, personas_semana2, color='red', label='Semana 2')
ax.set_xlabel('Mochilas')
ax.set_ylabel('Personas')
ax.set_title('Superposición de Gráficas de Dispersión - Semana 1 vs Semana 2')
ax.legend()
plt.show()
#=======================================================================
#semana1-semana2-semana3
#=======================================================================
fig, ax = plt.subplots()
ax.scatter(mochilas_semana1, personas_semana1, color='blue', label='Semana 1')
ax.scatter(mochilas_semana2, personas_semana2, color='red', label='Semana 2')
ax.scatter(mochilas_semana3, personas_semana3, color='green', label='Semana 3')
ax.set_xlabel('Mochilas')
ax.set_ylabel('Personas')
ax.set_title('Superposición de Gráficas de Dispersión - Semana 1 vs Semana 2 vs Semana 3')
ax.legend()
plt.show()
#=======================================================================
#semana1-semana2-semana3-semana4
#=======================================================================
fig, ax = plt.subplots()
ax.scatter(mochilas_semana1, personas_semana1, color='blue', label='Semana 1')
ax.scatter(mochilas_semana2, personas_semana2, color='red', label='Semana 2')
ax.scatter(mochilas_semana3, personas_semana3, color='green', label='Semana 3')
ax.scatter(mochilas_semana4, personas_semana4, color='orange', label='Semana 4')
ax.set_xlabel('Mochilas')
ax.set_ylabel('Personas')
ax.set_title('Superposición de Gráficas de Dispersión - Semana 1 vs Semana 2 vs Semana 3 vs Semana 4')
ax.legend()
plt.show()
#=======================================================================
#semana1-semana2-semana3-semana4-semana5
#=======================================================================
fig, ax = plt.subplots()
ax.scatter(mochilas_semana1, personas_semana1, color='blue', label='Semana 1')
ax.scatter(mochilas_semana2, personas_semana2, color='red', label='Semana 2')
ax.scatter(mochilas_semana3, personas_semana3, color='green', label='Semana 3')
ax.scatter(mochilas_semana4, personas_semana4, color='orange', label='Semana 4')
ax.scatter(mochilas_semana5, personas_semana5, color='purple', label='Semana 5')
ax.set_xlabel('Mochilas')
ax.set_ylabel('Personas')
ax.set_title('Superposición de Gráficas de Dispersión - Semana 1 vs Semana 2 vs Semana 3 vs Semana 4 vs Semana 5')
ax.legend()
plt.show()
