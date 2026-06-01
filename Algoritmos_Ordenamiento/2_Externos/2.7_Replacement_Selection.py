# Librería para trabajar con heaps (montículos)
# Permite obtener rápidamente el elemento más pequeño
import heapq


# Genera un run ordenado utilizando un heap
def replacement_selection(datos):

    # Convertir la lista en un heap
    # Después de esto el menor elemento estará accesible
    heapq.heapify(datos)

    # Aquí se guardará el run generado
    run = []

    # Continuar mientras existan elementos en el heap
    while datos:

        # Extraer el elemento más pequeño
        menor = heapq.heappop(datos)

        # Agregarlo al run actual
        run.append(menor)

    # Regresar el run generado
    return run


datos = [8, 3, 7, 1, 5, 2, 9]

print(replacement_selection(datos))