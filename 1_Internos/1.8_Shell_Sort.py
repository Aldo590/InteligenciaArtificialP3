# Función principal de Shell Sort
def shell_sort(lista):

    # Cantidad de elementos
    n = len(lista)

    # El gap inicial será la mitad de la lista
    gap = n // 2

    # Continuar mientras el gap sea mayor que cero
    while gap > 0:

        # Recorrer los elementos desde la posición gap
        for i in range(gap, n):

            # Guardar el elemento actual
            temp = lista[i]

            # Posición que se utilizará para comparar
            j = i

            # Comparar elementos separados por el gap actual
            while j >= gap and lista[j - gap] > temp:

                # Desplazar el elemento mayor hacia la derecha
                lista[j] = lista[j - gap]

                # Retroceder otro gap
                j -= gap

            # Insertar el elemento en su posición correcta
            lista[j] = temp

        # Reducir el gap para hacer comparaciones más cercanas
        gap //= 2

    # Regresar la lista ordenada
    return lista


numeros = [8, 5, 3, 7, 6, 2, 1, 4]

print(shell_sort(numeros))