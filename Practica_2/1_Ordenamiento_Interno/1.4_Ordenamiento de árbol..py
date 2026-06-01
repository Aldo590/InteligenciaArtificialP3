# Nodo del árbol binario
class Nodo:

    # Constructor
    def __init__(self, valor):

        # Valor almacenado
        self.valor = valor

        # Hijo izquierdo
        self.izquierda = None

        # Hijo derecho
        self.derecha = None


# Insertar un valor en el árbol
def insertar(raiz, valor):

    # Si no existe nodo, crearlo
    if raiz is None:

        return Nodo(valor)

    # Si el valor es menor, va a la izquierda
    if valor < raiz.valor:

        raiz.izquierda = insertar(raiz.izquierda, valor)

    # Si es mayor o igual, va a la derecha
    else:

        raiz.derecha = insertar(raiz.derecha, valor)

    # Regresar la raíz
    return raiz


# Recorrido Inorder
def inorder(raiz, resultado):

    # Si existe nodo
    if raiz:

        # Recorrer izquierda
        inorder(raiz.izquierda, resultado)

        # Guardar valor actual
        resultado.append(raiz.valor)

        # Recorrer derecha
        inorder(raiz.derecha, resultado)


# Función principal
def tree_sort(lista):

    # Árbol inicialmente vacío
    raiz = None

    # Insertar cada elemento
    for valor in lista:

        raiz = insertar(raiz, valor)

    # Lista resultado
    resultado = []

    # Obtener elementos ordenados
    inorder(raiz, resultado)

    return resultado


numeros = [5, 2, 9, 1, 7]

print(tree_sort(numeros))