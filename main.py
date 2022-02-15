#Importanción de recursos de una Interfaz de línea de comandos y un invocable.
import random


def bucket_sort(arreglo):
    #Inicialización de variables
    mayor = max(arreglo)
    tamaño = len(arreglo)
    size = mayor / tamaño
    buckets = [[] for _ in range(tamaño)]

    #Establecer el rango
    for i in range(tamaño):
        j = int(arreglo[i] / size)
        if j != tamaño:
            buckets[j].append(arreglo[i])
        else:
            buckets[tamaño - 1].append(arreglo[i])

    #Ordenar todos los elementos de cada cubeta
    for i in range(tamaño):
        insertion_sort(buckets[i])

    #Ordenar cada elementos entre cubetas
    resultado = []
    for i in range(tamaño):
        resultado = resultado + buckets[i]

    return resultado


def insertion_sort(arreglo):
    for i in range(1, len(arreglo)):
        temp = arreglo[i]
        j = i - 1
        while (j >= 0 and temp < arreglo[j]):
            arreglo[j + 1] = arreglo[j]
            j = j - 1
        arreglo[j + 1] = temp


#arreglo = input("Ingrese los elementos a ordenar =>").split()
arreglo = []
for i in range(100000):
    arreglo.append(random.randint(1, 100))

#arreglo = [int(x) for x in arreglo]
from time import time
start_time = time()
lista_ordenada = bucket_sort(arreglo)
elapsed_time = time() - start_time

print('Lista Ordenada: ', end='')
print(lista_ordenada)

print("Elapsed time: %.10f seconds." % elapsed_time)
