# Librería para trabajar con heaps (montículos)
# Permite obtener rápidamente el elemento más pequeño
import heapq

# Función que mezcla varias listas ordenadas
def multiway_merge(listas):

    # Montículo donde se almacenarán los elementos candidatos
    heap = []

    # Lista donde se guardará el resultado final
    resultado = []

    # Insertar el primer elemento de cada lista
    for i, lista in enumerate(listas):

        # Verificar que la lista no esté vacía
        if lista:

            # Guardar:
            # valor, número de lista y posición dentro de la lista
            heapq.heappush(heap, (lista[0], i, 0))

    # Continuar mientras existan elementos por procesar
    while heap:

        # Obtener el elemento más pequeño disponible
        valor, lista_idx, elem_idx = heapq.heappop(heap)

        # Agregarlo al resultado
        resultado.append(valor)

        # Calcular la posición del siguiente elemento
        # de la misma lista
        siguiente = elem_idx + 1

        # Verificar si aún quedan elementos
        if siguiente < len(listas[lista_idx]):

            # Insertar el siguiente elemento de esa lista
            # para que participe en futuras comparaciones
            heapq.heappush(
                heap,
                (
                    listas[lista_idx][siguiente],
                    lista_idx,
                    siguiente
                )
            )

    # Regresar la lista completamente ordenada
    return resultado


listas = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print(multiway_merge(listas))