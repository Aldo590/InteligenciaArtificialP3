# Lista desordenada que queremos ordenar
numeros = [5, 2, 9, 1, 7]

# Recorremos toda la lista
for i in range(len(numeros)):

    # Suponemos que el menor elemento está en la posición actual
    indice_menor = i

    # Buscamos si existe un elemento más pequeño
    # en el resto de la lista
    for j in range(i + 1, len(numeros)):

        # Si encontramos un valor menor
        if numeros[j] < numeros[indice_menor]:

            # Actualizamos la posición del menor
            indice_menor = j

    # Intercambiamos el elemento actual
    # con el menor encontrado
    numeros[i], numeros[indice_menor] = numeros[indice_menor], numeros[i]

# Mostramos la lista ordenada
print("Lista ordenada:")
print(numeros)