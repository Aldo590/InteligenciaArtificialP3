# Función principal
def counting_sort(lista):

    # Obtener el valor máximo
    maximo = max(lista)

    # Crear arreglo de conteo
    conteo = [0] * (maximo + 1)

    # Contar cuántas veces aparece cada número
    for numero in lista:

        conteo[numero] += 1

    # Lista donde se guardará el resultado
    resultado = []

    # Recorrer todos los valores posibles
    for numero in range(len(conteo)):

        # Agregar el número tantas veces
        # como apareció
        for _ in range(conteo[numero]):

            resultado.append(numero)

    # Regresar lista ordenada
    return resultado


numeros = [4, 2, 2, 8, 3, 3, 1]

print(counting_sort(numeros))