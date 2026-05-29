# Lista desordenada que queremos ordenar
numeros = [5, 2, 9, 1, 7]

# Recorremos la lista desde el segundo elemento
# Empezamos en 1 porque el primer elemento se considera ya ordenado
for i in range(1, len(numeros)):

    # Guardamos el valor actual que vamos a insertar
    actual = numeros[i]

    # j será el índice del elemento anterior
    j = i - 1

    # Mientras:
    # 1. j sea válido
    # 2. el elemento anterior sea mayor que el actual
    while j >= 0 and numeros[j] > actual:

        # Movemos el elemento una posición a la derecha
        numeros[j + 1] = numeros[j]

        # Retrocedemos una posición
        j = j - 1

    # Insertamos el valor actual en la posición correcta
    numeros[j + 1] = actual

# Mostramos la lista ya ordenada
print("Lista ordenada:")
print(numeros)