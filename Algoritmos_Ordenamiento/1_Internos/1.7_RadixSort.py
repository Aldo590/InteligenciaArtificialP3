# Ordena la lista según un dígito específico
def counting_sort(lista, exp):

    # Cantidad de elementos
    n = len(lista)

    # Lista auxiliar
    salida = [0] * n

    # Arreglo para contar dígitos del 0 al 9
    conteo = [0] * 10

    # Contar cuántas veces aparece cada dígito
    for numero in lista:

        # Obtener el dígito actual
        indice = (numero // exp) % 10

        # Incrementar contador
        conteo[indice] += 1

    # Acumular los conteos
    for i in range(1, 10):

        conteo[i] += conteo[i - 1]

    # Construir la lista ordenada
    for i in range(n - 1, -1, -1):

        # Obtener el dígito actual
        indice = (lista[i] // exp) % 10

        # Colocar el número en su posición
        salida[conteo[indice] - 1] = lista[i]

        # Actualizar contador
        conteo[indice] -= 1

    # Copiar el resultado a la lista original
    for i in range(n):

        lista[i] = salida[i]


# Función principal de Radix Sort
def radix_sort(lista):

    # Obtener el número más grande
    maximo = max(lista)

    # Empezar por las unidades
    exp = 1

    # Recorrer unidades, decenas, centenas, etc.
    while maximo // exp > 0:

        # Ordenar según el dígito actual
        counting_sort(lista, exp)

        # Pasar al siguiente dígito
        exp *= 10

    # Regresar la lista ordenada
    return lista


# Lista de ejemplo
numeros = [170, 45, 75, 90, 802, 24, 2, 66]

# Mostrar resultado
print(radix_sort(numeros))