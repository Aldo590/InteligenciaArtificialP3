# Librería para trabajar con heaps (montículos)
# Un heap permite obtener rápidamente
# el elemento más pequeño disponible
import heapq


# Función que mezcla varios runs ordenados
def k_way_merge(runs):

    # Heap donde se almacenarán los candidatos
    # al siguiente elemento del resultado
    heap = []

    # Lista donde se guardará el resultado final
    resultado = []

    # Insertar el primer elemento de cada run
    for run_idx, run in enumerate(runs):

        # Verificar que el run tenga elementos
        if run:

            # Insertar en el heap:
            # valor, número de run y posición dentro del run
            heapq.heappush(heap, (run[0], run_idx, 0))

    # Continuar mientras existan elementos por procesar
    while heap:

        # Extraer el elemento más pequeño del heap
        valor, run_idx, pos = heapq.heappop(heap)

        # Agregarlo al resultado final
        resultado.append(valor)

        # Calcular la siguiente posición dentro del mismo run
        siguiente = pos + 1

        # Verificar si aún quedan elementos en ese run
        if siguiente < len(runs[run_idx]):

            # Insertar el siguiente elemento del run
            # para que participe en futuras comparaciones
            heapq.heappush(
                heap,
                (
                    runs[run_idx][siguiente],
                    run_idx,
                    siguiente
                )
            )

    # Regresar la lista completamente ordenada
    return resultado


runs = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print(k_way_merge(runs))