import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def promedio(data):
    #Calicaciones tiene datos del tipo flotante
    #El ranto de calificaciones esta definido por el conjunto [6,10]?
    #Cualquier valor fuera de ellos en N/A
    #Podemos describir el promedio de las calificaciones de la UAQ
    #sacando la formula de promedio

    longitud_cal=len(data)
    #variables globales
    total=0
    for i in range(longitud_cal):
        calif_estudiante=data[i]
        calif_estudiante=float(calif_estudiante)
        #si yo ya puedo acceder a las calificaciones
        #me hace falta sumar
        total+=calif_estudiante

    promedio=total/int(longitud_cal)
    promedio=round(promedio,2)
    #print(f"El primedio de la muestra ha sido {round(promedio,2)}")
    return promedio
    
def mediana(data):
    longitud_cal=len(data)
    #tenemos que saber si la longitud es par o es impar
    if (longitud_cal%2==0):
        #Es par
        salida="par"
    else:
        #Es impar
        salida="impar"

    if(salida=="par"):
        mitad=longitud_cal/2
        mitad=int(mitad-1)
        mitad2=mitad+1
        mitad2=int(mitad2)
        mediana=data[mitad]+data[mitad2]
        mediana=float(mediana)/2
        mediana=round(mediana,2)
        #print(round(mediana,2))
    else:
        mitad=longitud_cal/2
        mitad=round(mitad)
        mediana=data[mitad]
        mediana=round(mediana,2)
        #print(mediana)
    return mediana

def varianza(data, promedio):

    #Necesitamos una sumatioria
    #definimos variable
    sumatoria=0
    
    #un ciclo que recorra todas las observaciones
    for x in data:
        sumatoria+=(x-promedio)**2
        
    #cuando la sumatioria este completa usar 2 decimales y usar round
    sumatoria=round(sumatoria,10)
    #Ya redondeado se hace la division
    longitud=len(data)
    varianza=round(sumatoria/(longitud-1),10)
    
    return varianza
def desviacionEstandar(data):
    return(math.sqrt(data))
def correlacion(data1, data2,promedio1,promedio2):
    longi=len(data1)
    sumatoria=0
    for x in range(longi):
        sumatoria+=data1[x]*data2[x]
    cor=((sumatoria/longi)-(promedio1*promedio2))
    return cor

#Leer el archivo csv
df=pd.read_csv("DATAGRAFICO.csv") #almacenamos en un dataframe los datos para generar los graficos
semana=df["Semana"] #un data frame para las semanas
dia=df["Dia"] #un dataframe para los dias
personas=df["Personas"] #un dataframe para las personas
mochilas=df["Mochilas"] #un dataframe para las mochilas

#semana1 filtrada son un dataframe donde se juntan todos los datos que correspondan al lunes de la semana 1
filtered_semana1 = df[df['Dia'] == 'Lunes']
personas_list1 = filtered_semana1['Personas'].tolist() #enlistamos todas las personas del lunes de la semana 1
mochilas_list1 = filtered_semana1['Mochilas'].tolist() #enlistamos todas las mochilas del lunes de la semana 1


#datos del lunes de la semana 3 en un dataframe...
filtered_semana2 = df[df['Dia'] == 'Martes']
personas_list2 = filtered_semana2['Personas'].tolist() #enlistamos todas las personas del martes de la semana 1
mochilas_list2 = filtered_semana2['Mochilas'].tolist() #enlistamos todas las mochilas del martes de la semana 1

#datos del lunes de la semana 3 en un dataframe...
filtered_semana3 = df[df['Dia'] == 'Miercoles']
personas_list3 = filtered_semana3['Personas'].tolist() #lista para personas
mochilas_list3 = filtered_semana3['Mochilas'].tolist() #lista para mochilas

#datos del lunes de la semana4 en un dataframe...
filtered_semana4 = df[df['Dia'] == 'Jueves']
personas_list4 = filtered_semana4['Personas'].tolist() #lista para personas
mochilas_list4 = filtered_semana4['Mochilas'].tolist() #lista para mochilas


hora=[]
#con un ciclo for, creamos el eje x del mismo tamaño para mostrar los datos en una grafica.
for i in range(len(personas_list1)):
    hora.append(i)
    
#se grafican los datos comparando dos datos (mochilas )
plt.plot(hora, mochilas_list1, label="Lunes", marker='o') 
plt.plot(hora, mochilas_list2, label="Miercoles", marker='s')
plt.xlabel('Horas')
plt.ylabel('Cantidad')
plt.title('Grafico de el UAQibus - Mochilas')
plt.legend()
plt.grid(True)
plt.show()
#se grafican los datos comparando dos datos (personas)
plt.plot(hora, personas_list1, label="Lunes", marker='o') 
plt.plot(hora, personas_list2, label="Miercoles", marker='s')
plt.xlabel('Horas')
plt.ylabel('Cantidad')
plt.title('Grafico de el UAQibus - Personas')
plt.legend()
plt.grid(True)
plt.show()

#=============================================================
#proceso para sacar las estadísticas.
#=============================================================
#ordenamos las listas
mochilas_list1.sort() 
mochilas_list2.sort()
mochilas_list3.sort()
mochilas_list4.sort()
personas_list1.sort()
personas_list2.sort()
personas_list3.sort()
personas_list4.sort()
#guardamos el promedio de cada lista en una nueva variable
promedio1=promedio(mochilas_list1)
promedio2=promedio(mochilas_list2)
promedio3=promedio(mochilas_list3)
promedio4=promedio(mochilas_list4)
promedio5=promedio(personas_list1)
promedio6=promedio(personas_list2)
promedio7=promedio(personas_list3)
promedio8=promedio(personas_list4)
#guardamos la mediana de cada lista en una nueva variable
mediana1=mediana(mochilas_list1)
mediana2=mediana(mochilas_list2)
mediana3=mediana(mochilas_list3)
mediana4=mediana(mochilas_list4)
mediana5=mediana(personas_list1)
mediana6=mediana(personas_list2)
mediana7=mediana(personas_list3)
mediana8=mediana(personas_list4)
#guardamos la varianza de cada lista en una variable
varianza1=varianza(mochilas_list1,promedio1)
varianza2=varianza(mochilas_list2,promedio2)
varianza3=varianza(mochilas_list3,promedio3)
varianza4=varianza(mochilas_list4,promedio4)
varianza5=varianza(personas_list1,promedio5)
varianza6=varianza(personas_list2,promedio6)
varianza7=varianza(personas_list3,promedio7)
varianza8=varianza(personas_list4,promedio8)
#guardamos la desviación estandar de cada grupo de datos en una variable
desv1=desviacionEstandar(varianza1)
desv2=desviacionEstandar(varianza2)
desv3=desviacionEstandar(varianza3)
desv4=desviacionEstandar(varianza4)
desv5=desviacionEstandar(varianza5)
desv6=desviacionEstandar(varianza6)
desv7=desviacionEstandar(varianza7)
desv8=desviacionEstandar(varianza8)

correla=correlacion(mochilas_list1,mochilas_list3,promedio1,promedio3)
print(f'La correlación lineal obtenida es de {correla}')
#obtenemos la relacion lineal y la almacenamos en la variable r
r=(correla/(desv1*desv2))
print(f'El coeficiente de correlacion es: {r}')

correla=correlacion(personas_list1,personas_list3,promedio5,promedio7)
print(f'La correlación lineal obtenida es de {correla}')
#obtenemos la relacion lineal y la almacenamos en la variable r
r=(correla/(desv1*desv2))
print(f'El coeficiente de correlacion es: {r}')