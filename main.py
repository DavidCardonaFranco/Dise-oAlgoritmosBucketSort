def bucket_sort(arreglo):

    mayor = max(arreglo)
    tamaño = len(arreglo)
    size = mayor / tamaño

    buckets = [[] for _ in range(tamaño)]

    for i in range(tamaño):
        j = int(arreglo[i] / size)
        if j != tamaño:
            buckets[j].append(arreglo[i])
        else:
            buckets[tamaño - 1].append(arreglo[i])

    for i in range(tamaño):
        insertion_sort(buckets[i])

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


arreglo = input("Ingrese los elementos a ordenar =>").split()
arreglo = [int(x) for x in arreglo]
lista_ordenada = bucket_sort(arreglo)
print('Lista Ordenada: ', end='')
print(lista_ordenada)