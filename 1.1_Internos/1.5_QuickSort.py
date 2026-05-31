# Función QuickSort
def quicksort(lista):

    # Si la lista tiene 0 o 1 elementos,
    # ya está ordenada
    if len(lista) <= 1:

        return lista

    # Elegir el primer elemento como pivote
    pivote = lista[0]

    # Lista de menores
    menores = []

    # Lista de mayores
    mayores = []

    # Recorrer todos los elementos excepto el pivote
    for elemento in lista[1:]:

        # Si es menor o igual al pivote
        if elemento <= pivote:

            menores.append(elemento)

        # Si es mayor
        else:

            mayores.append(elemento)

    # Ordenar recursivamente y unir resultados
    return quicksort(menores) + [pivote] + quicksort(mayores)


numeros = [5, 2, 9, 1, 7]

print(quicksort(numeros))