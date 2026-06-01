# Función principal
def distribution_sort(datos):

    # Grupo para valores menores a 100
    grupo1 = []

    # Grupo para valores entre 100 y 199
    grupo2 = []

    # Grupo para valores mayores o iguales a 200
    grupo3 = []

    # Distribuir los elementos en grupos
    for numero in datos:

        # Si pertenece al primer rango
        if numero < 100:

            grupo1.append(numero)

        # Si pertenece al segundo rango
        elif numero < 200:

            grupo2.append(numero)

        # Si pertenece al tercer rango
        else:

            grupo3.append(numero)

    # Ordenar cada grupo por separado
    grupo1.sort()
    grupo2.sort()
    grupo3.sort()

    # Unir los grupos en orden
    resultado = grupo1 + grupo2 + grupo3

    # Regresar la lista ordenada
    return resultado


datos = [250, 75, 180, 30, 220, 150, 90]

print(distribution_sort(datos))