# Une dos listas ya ordenadas
def straight_merge(lista1, lista2):

    # Lista resultado
    resultado = []

    # Índice para la primera lista
    i = 0

    # Índice para la segunda lista
    j = 0

    # Comparar elementos de ambas listas
    while i < len(lista1) and j < len(lista2):

        # Si el elemento de lista1 es menor
        if lista1[i] < lista2[j]:

            # Agregar a resultado
            resultado.append(lista1[i])

            # Avanzar índice
            i += 1

        else:

            # Agregar elemento de lista2
            resultado.append(lista2[j])

            # Avanzar índice
            j += 1

    # Agregar elementos restantes de lista1
    resultado.extend(lista1[i:])

    # Agregar elementos restantes de lista2
    resultado.extend(lista2[j:])

    # Regresar resultado
    return resultado


# Ejemplo
a = [1, 4, 7]
b = [2, 5, 8]

print(straight_merge(a, b))