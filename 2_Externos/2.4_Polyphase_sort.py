# Función principal
def polyphase_sort(runs):

    # Continuar hasta que solo quede un run
    while len(runs) > 1:

        # Guardará los nuevos runs generados
        nueva = []

        # Tomar los runs de dos en dos
        for i in range(0, len(runs) - 1, 2):

            # Mezclar dos runs ordenados
            nueva.append(merge(runs[i], runs[i + 1]))

        # Si quedó un run sin pareja
        if len(runs) % 2 == 1:

            # Pasarlo directamente a la siguiente ronda
            nueva.append(runs[-1])

        # Actualizar los runs disponibles
        runs = nueva

    # El único run restante contiene
    # todos los elementos ordenados
    return runs[0]


# Función que mezcla dos listas ordenadas
def merge(a, b):

    # Lista resultado
    resultado = []

    # Posición actual en la primera lista
    i = 0

    # Posición actual en la segunda lista
    j = 0

    # Comparar elementos mientras ambas listas tengan datos
    while i < len(a) and j < len(b):

        # Si el elemento de la primera lista es menor
        if a[i] < b[j]:

            # Agregarlo al resultado
            resultado.append(a[i])

            # Avanzar en la primera lista
            i += 1

        else:

            # Agregar el elemento de la segunda lista
            resultado.append(b[j])

            # Avanzar en la segunda lista
            j += 1

    # Agregar los elementos restantes de la primera lista
    resultado.extend(a[i:])

    # Agregar los elementos restantes de la segunda lista
    resultado.extend(b[j:])

    return resultado


runs = [
    [1, 5],
    [2, 6],
    [3, 7],
    [4, 8]
]

print(polyphase_sort(runs))