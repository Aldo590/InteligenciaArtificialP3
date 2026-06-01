# Ordena según un dígito específico
def counting_sort(lista, exp):

    # Cantidad de elementos
    n = len(lista)

    # Lista auxiliar para construir el resultado
    salida = [0] * n

    # Arreglo para contar los dígitos del 0 al 9
    conteo = [0] * 10

    # Contar cuántas veces aparece cada dígito
    for numero in lista:

        # Obtener el dígito correspondiente
        indice = (numero // exp) % 10

        conteo[indice] += 1

    # Transformar los conteos en posiciones
    for i in range(1, 10):

        conteo[i] += conteo[i - 1]

    # Construir la salida ordenada
    # Se recorre de derecha a izquierda para conservar estabilidad
    for i in range(n - 1, -1, -1):

        # Obtener el dígito actual
        indice = (lista[i] // exp) % 10

        # Colocar el elemento en su posición correcta
        salida[conteo[indice] - 1] = lista[i]

        # Actualizar la posición disponible
        conteo[indice] -= 1

    # Copiar el resultado a la lista original
    for i in range(n):

        lista[i] = salida[i]


# Función principal
def external_radix_sort(lista):

    # Obtener el valor más grande
    maximo = max(lista)

    # Comenzar con las unidades
    exp = 1

    # Procesar unidades, decenas, centenas, etc.
    while maximo // exp > 0:

        # Ordenar según el dígito actual
        counting_sort(lista, exp)

        # Pasar al siguiente dígito
        exp *= 10

    # Regresar la lista ordenada
    return lista


datos = [170, 45, 75, 90, 802, 24, 2, 66]

print(external_radix_sort(datos))