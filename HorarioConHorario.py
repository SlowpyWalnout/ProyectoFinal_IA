import csv
import matplotlib.pyplot as plt

# Definir los arrays
hora = []
mochilas = []
personas = []

# Leer el archivo CSV
with open('Datos_Graficas.csv', newline='') as csvfile:
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
hora_dividida = dividir_lista(hora, tamano_sublista)
mochilas_divididas = dividir_lista(mochilas, tamano_sublista)
personas_divididas = dividir_lista(personas, tamano_sublista)

# Crear la nueva lista que simula ser la original pero dividida
lista_dividida = list(zip(hora_dividida, mochilas_divididas, personas_divididas))
i = 0
datos = []
for semana in lista_dividida:
    tamano_sublista = 21
    horarios_semana = dividir_lista(semana[0], tamano_sublista)
    mochilas_semana = dividir_lista(semana[1], tamano_sublista)
    personas_semana = dividir_lista(semana[2], tamano_sublista)
    nueva_lista_dividida = list(zip(horarios_semana, mochilas_semana, personas_semana))
    datos.append(nueva_lista_dividida)
    

datos_dia = []
i = 0
for semana in datos:
    for dia in semana:
        
        tamano_sublista = 7
        horario_dia = dividir_lista(dia[0], tamano_sublista)
        mochilas_dia = dividir_lista(dia[1], tamano_sublista)
        personas_dia = dividir_lista(dia[2], tamano_sublista)
         
        print(horario_dia)
        print(mochilas_dia)
        print(personas_dia)
        
        ##grafica de hora 0 vs hora 1 (3-5)
        
        # Datos del primer conjunto
        horario_hora_1 = horario_dia[0]
        mochilas_hora_1 = mochilas_dia[0]
        personas_hora_1 = personas_dia[0]

        # Datos del segundo conjunto
        horario_hora_2 = horario_dia[1]
        mochilas_hora_2 = mochilas_dia[1]
        personas_hora_2 = personas_dia[1]

        # Crear una sola gráfica de dispersión
        fig, ax = plt.subplots()

        # Superponer las dos gráficas de dispersión
        ax.scatter(mochilas_hora_1, personas_hora_1, label='Horario A')
        ax.scatter(mochilas_hora_2, personas_hora_2, label='Horario B')

        # Configuración de la gráfica
        ax.set_xlabel('Mochilas')
        ax.set_ylabel('Personas')
        ax.set_title('comparacion de Gráficas de horario A vs Horario B')
        ax.legend()

        # Mostrar la gráfica
        plt.show()

        ##grafica de hora 1 vs hora 2 (5-7)
        # Datos del primer conjunto
        horario_hora_1 = horario_dia[0]
        mochilas_hora_1 = mochilas_dia[0]
        personas_hora_1 = personas_dia[0]

        # Datos del segundo conjunto
        horario_hora_2 = horario_dia[2]
        mochilas_hora_2 = mochilas_dia[2]
        personas_hora_2 = personas_dia[2]

        # Crear una sola gráfica de dispersión
        fig, ax = plt.subplots()

        # Superponer las dos gráficas de dispersión
        ax.scatter(mochilas_hora_1, personas_hora_1, label='Horario A')
        ax.scatter(mochilas_hora_2, personas_hora_2, label='Horario C')

        # Configuración de la gráfica
        ax.set_xlabel('Mochilas')
        ax.set_ylabel('Personas')
        ax.set_title('comparacion de Gráficas de horario A vs Horario C')
        ax.legend()

        # Mostrar la gráfica
        plt.show()
        
        
        ##grafica de hora 2 vs 0 (7-1)
        # Datos del primer conjunto
        horario_hora_1 = horario_dia[1]
        mochilas_hora_1 = mochilas_dia[1]
        personas_hora_1 = personas_dia[1]

        # Datos del segundo conjunto
        horario_hora_2 = horario_dia[2]
        mochilas_hora_2 = mochilas_dia[2]
        personas_hora_2 = personas_dia[2]

        # Crear una sola gráfica de dispersión
        fig, ax = plt.subplots()

        # Superponer las dos gráficas de dispersión
        ax.scatter(mochilas_hora_1, personas_hora_1, label='Horario B')
        ax.scatter(mochilas_hora_2, personas_hora_2, label='Horario C')

        # Configuración de la gráfica
        ax.set_xlabel('Mochilas')
        ax.set_ylabel('Personas')
        ax.set_title('comparacion de Gráficas de horario A vs Horario B')
        ax.legend()

        # Mostrar la gráfica
        plt.show()
    print('se acabo la semana')
