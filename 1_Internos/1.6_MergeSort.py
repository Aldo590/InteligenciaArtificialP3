# Función principal
def mergesort(lista):

    # Si hay 0 o 1 elementos
    if len(lista) <= 1:

        return lista

    # Calcular punto medio
    medio = len(lista) // 2

    # Dividir parte izquierda
    izquierda = mergesort(lista[:medio])

    # Dividir parte derecha
    derecha = mergesort(lista[medio:])

    # Combinar ambas partes
    return fusionar(izquierda, derecha)


# Función para unir listas ordenadas
def fusionar(izquierda, derecha):

    # Lista resultado
    resultado = []

    # Índice de izquierda
    i = 0

    # Índice de derecha
    j = 0

    # Comparar elementos
    while i < len(izquierda) and j < len(derecha):

        # Si el elemento izquierdo es menor
        if izquierda[i] < derecha[j]:

            resultado.append(izquierda[i])

            i += 1

        # Si el derecho es menor
        else:

            resultado.append(derecha[j])

            j += 1

    # Agregar elementos sobrantes
    resultado.extend(izquierda[i:])

    # Agregar elementos sobrantes
    resultado.extend(derecha[j:])

    return resultado


numeros = [5, 2, 9, 1, 7]

print(mergesort(numeros))