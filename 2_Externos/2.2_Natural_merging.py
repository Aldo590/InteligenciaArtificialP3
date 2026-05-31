# Función principal de Natural Merging
def natural_merge(lista):

    # Si la lista tiene 0 o 1 elementos,
    # ya se considera ordenada
    if len(lista) <= 1:
        return lista

    # Aquí se guardarán los runs encontrados
    runs = []

    # El primer run comienza con el primer elemento
    actual = [lista[0]]

    # Recorrer la lista desde el segundo elemento
    for i in range(1, len(lista)):

        # Comparar el elemento actual con el anterior
        if lista[i] >= lista[i - 1]:

            # Como sigue el orden ascendente,
            # pertenece al mismo run
            actual.append(lista[i])

        else:

            # El orden se rompió,
            # el run actual termina
            runs.append(actual)

            # Comenzar un nuevo run
            actual = [lista[i]]

    # Guardar el último run encontrado
    runs.append(actual)

    # Mientras exista más de un run,
    # seguir mezclándolos
    while len(runs) > 1:

        # Guardará los nuevos runs generados
        nueva = []

        # Tomar los runs de dos en dos
        for i in range(0, len(runs) - 1, 2):

            # Mezclar dos runs ordenados
            nueva.append(merge(runs[i], runs[i + 1]))

        # Si quedó un run sin pareja
        if len(runs) % 2 == 1:

            # Pasa directamente a la siguiente ronda
            nueva.append(runs[-1])

        # Actualizar los runs disponibles
        runs = nueva

    # El único run restante contiene
    # todos los elementos ordenados
    return runs[0]


# Función que mezcla dos listas ordenadas
def merge(a, b):

    # Lista donde se guardará el resultado
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


numeros = [3, 5, 8, 2, 4, 7, 1, 9]

print(natural_merge(numeros))