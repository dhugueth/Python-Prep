
import sys

if len(sys.argv)==2:

    import datetime
    import os

    marca_de_tiempo=datetime.datetime.now()
    marca_de_tiempo=int(datetime.datetime.timestamp(marca_de_tiempo))

    lluvia=sys.argv[1]
    temperatura=input('Ingrese la temperatura en grados celsius (°C): ')
    humedad=input('Ingrese el porcentaje de humedad: ')

    linea_a_escribir = str(marca_de_tiempo) + ',' + humedad + ',' + temperatura + ',' + lluvia

    logs_lluvia=open('09 - Entrada-Salida y Manejo de Archivos\Dani_clase_9_ej2.csv' , 'a')
    logs_lluvia.write(linea_a_escribir+'\n')
    logs_lluvia.close()

else:
    print("ERROR: debe ingresar si llovio o no llovio")
    print('Ejemplo: Dani_clase_9_ej2.py <True o False>')