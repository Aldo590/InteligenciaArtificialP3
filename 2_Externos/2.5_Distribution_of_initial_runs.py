# Función que detecta runs naturales
def initial_runs(lista):

    # Aquí se guardarán todos los runs encontrados
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
            # guardar el run actual
            runs.append(actual)

            # Comenzar un nuevo run
            actual = [lista[i]]

    # Guardar el último run encontrado
    runs.append(actual)

    # Regresar todos los runs encontrados
    return runs


numeros = [1, 3, 5, 2, 4, 8, 1, 6]

print(initial_runs(numeros))