# Función que ordena una lista usando Bubble Sort
def bubble_sort(lista):

    # Obtener la cantidad de elementos de la lista
    n = len(lista)

    # Ciclo externo:
    # Controla cuántas pasadas se harán sobre la lista
    for i in range(n):

        # Ciclo interno:
        # Compara elementos vecinos
        # En cada pasada el mayor elemento queda al final,
        # por eso restamos i
        for j in range(0, n - i - 1):

            # Si el elemento actual es mayor que el siguiente
            if lista[j] > lista[j + 1]:

                # Intercambiar posiciones
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    # Devolver la lista ordenada
    return lista


# Lista de ejemplo
numeros = [5, 2, 9, 1, 7]

# Mostrar resultado
print(bubble_sort(numeros))