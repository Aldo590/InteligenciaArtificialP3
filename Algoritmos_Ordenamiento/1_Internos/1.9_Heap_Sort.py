# Ajusta un subárbol para mantener la propiedad de Max Heap
def heapify(lista, n, i):

    # Suponer que la raíz es el mayor elemento
    mayor = i

    # Índice del hijo izquierdo
    izquierda = 2 * i + 1

    # Índice del hijo derecho
    derecha = 2 * i + 2

    # Verificar si el hijo izquierdo existe
    # y es mayor que la raíz
    if izquierda < n and lista[izquierda] > lista[mayor]:

        mayor = izquierda

    # Verificar si el hijo derecho existe
    # y es mayor que el mayor actual
    if derecha < n and lista[derecha] > lista[mayor]:

        mayor = derecha

    # Si encontramos un elemento mayor que la raíz
    if mayor != i:

        # Intercambiar posiciones
        lista[i], lista[mayor] = lista[mayor], lista[i]

        # Repetir el proceso en el subárbol afectado
        heapify(lista, n, mayor)


# Función principal
def heap_sort(lista):

    # Cantidad de elementos
    n = len(lista)

    # Construir el Max Heap
    for i in range(n // 2 - 1, -1, -1):

        heapify(lista, n, i)

    # Extraer elementos uno por uno
    for i in range(n - 1, 0, -1):

        # Mover el mayor elemento al final
        lista[0], lista[i] = lista[i], lista[0]

        # Reconstruir el heap sin el elemento ya ordenado
        heapify(lista, i, 0)

    # Regresar la lista ordenada
    return lista


numeros = [4, 10, 3, 5, 1]

print(heap_sort(numeros))