# Librería para trabajar con grafos 
# Instalar: pip install networkx matplotlib
import networkx as nx

# Librería para crear gráficos
import matplotlib.pyplot as plt


# Algoritmo de Dijkstra
def dijkstra(grafo, inicio):

    # Diccionario donde se almacenarán
    # las distancias mínimas encontradas
    distancias = {}

    # Diccionario que almacena el nodo anterior
    # de cada nodo para reconstruir el camino
    anteriores = {}

    # Conjunto de nodos visitados
    visitados = set()

    # Inicializar todas las distancias en infinito
    for nodo in grafo:

        distancias[nodo] = float("inf")

        # Inicialmente no se conoce
        # ningún nodo anterior
        anteriores[nodo] = None

    # La distancia al nodo inicial es cero
    distancias[inicio] = 0

    # Contador para mostrar las iteraciones
    paso = 1

    # Continuar mientras existan nodos sin visitar
    while len(visitados) < len(grafo):

        # Nodo que se procesará en esta iteración
        nodo_actual = None

        # Distancia mínima encontrada
        distancia_minima = float("inf")

        # Buscar el nodo no visitado
        # con menor distancia
        for nodo in grafo:

            if nodo not in visitados and distancias[nodo] < distancia_minima:

                distancia_minima = distancias[nodo]
                nodo_actual = nodo

        # Si no existe un nodo alcanzable
        # terminar el algoritmo
        if nodo_actual is None:
            break

        # Mostrar un encabezado para separar visualmente
        # cada iteración del algoritmo
        print("\n" + "=" * 50)

        # Mostrar el número de paso actual
        print("PASO", paso)

        # Línea decorativa para mejorar la lectura
        print("=" * 50)

        # Mostrar cuál fue el nodo no visitado
        # con la menor distancia encontrada
        print("Nodo seleccionado:", nodo_actual)

        # Mostrar la distancia mínima acumulada
        # hasta llegar al nodo actual
        print(
            "Distancia acumulada:",
            distancias[nodo_actual]
        )

        # Marcar el nodo como visitado
        visitados.add(nodo_actual)

        # Mostrar los nodos visitados
        print(
            "Visitados:",
            sorted(visitados)
        )

        # Revisar todos los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():

            # Si el vecino ya fue visitado,
            # no es necesario volver a evaluarlo
            if vecino in visitados:

                continue

            # Mostrar la conexión que se está analizando
            print(
                f"\nEvaluando: {nodo_actual} -> {vecino}"
            )

            # Mostrar el peso de la conexión actual
            print(
                f"Peso de la arista: {peso}"
            )

            # Calcular la distancia pasando
            # por el nodo actual
            nueva_distancia = (
                distancias[nodo_actual] + peso
            )

            # Mostrar la mejor distancia conocida
            # hasta este momento para el vecino
            print(
                f"Distancia actual de {vecino}: "
                f"{distancias[vecino]}"
            )

            # Mostrar la distancia que se obtendría
            # si se pasa por el nodo actual
            print(
                f"Nueva distancia propuesta: "
                f"{nueva_distancia}"
            )

            # Si se encontró un camino mejor
            if nueva_distancia < distancias[vecino]:

                # Informar que se encontró una mejor ruta
                print(
                    "Se encontró un camino más corto."
                )

                # Guardar la nueva distancia mínima
                distancias[vecino] = nueva_distancia

                # Guardar desde qué nodo se llegó
                # al vecino usando el mejor camino
                anteriores[vecino] = nodo_actual

                # Mostrar el cambio realizado
                print(
                    f"Nueva distancia de {vecino}: "
                    f"{distancias[vecino]}"
                )

            else:

                # Informar que no hubo mejora
                print(
                    "No se actualiza la distancia."
                )

        # Mostrar las distancias al finalizar
        # la iteración actual
        print("\nDistancias actuales:")

        # Recorrer el diccionario de distancias
        for nodo in distancias:

            print(
                f"{nodo}: {distancias[nodo]}"
            )

        # Incrementar el contador de pasos
        paso += 1

    # Regresar distancias y caminos
    return distancias, anteriores


# Reconstruir el camino mínimo
def obtener_camino(anteriores, destino):

    # Aquí se almacenará el camino
    camino = []

    # Comenzar desde el destino
    actual = destino

    # Retroceder usando los nodos anteriores
    while actual is not None:

        # Agregar el nodo actual
        camino.append(actual)

        # Ir al nodo anterior
        actual = anteriores[actual]

    # Invertir el camino para que quede
    # desde el origen hasta el destino
    camino.reverse()

    # Regresar el camino completo
    return camino


# Mostrar el grafo final
def mostrar_grafo(grafo, camino):

    # Crear una estructura de grafo
    # compatible con NetworkX
    G = nx.Graph()

    # Agregar todas las conexiones
    for origen in grafo:

        for destino, peso in grafo[origen].items():

            # Agregar conexión y peso
            G.add_edge(
                origen,
                destino,
                weight=peso
            )

    # Calcular automáticamente la posición
    # de los nodos en la ventana
    pos = nx.spring_layout(
        G,
        seed=42
    )

    # Lista que almacenará únicamente
    # las conexiones del camino mínimo
    camino_aristas = []

    # Convertir la lista de nodos del camino
    # en pares de conexiones
    for i in range(len(camino) - 1):

        camino_aristas.append(
            (camino[i], camino[i + 1])
        )

    # Dibujar todos los nodos
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000
    )

    # Dibujar todas las conexiones en gris
    nx.draw_networkx_edges(
        G,
        pos,
        edge_color="gray",
        width=2
    )

    # Resaltar las conexiones que forman
    # el camino mínimo encontrado
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=camino_aristas,
        edge_color="red",
        width=4
    )

    # Obtener los pesos de cada conexión
    etiquetas = nx.get_edge_attributes(
        G,
        "weight"
    )

    # Mostrar los pesos sobre las conexiones
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=etiquetas
    )

    # Mostrar un título en la ventana
    plt.title(
        "Camino minimo encontrado por Dijkstra"
    )

    # Mostrar la gráfica final
    plt.show()


# Grafo de ejemplo
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

# Mostrar los nodos disponibles
print("Nodos disponibles:")

for nodo in grafo:

    print("-", nodo)

# Solicitar al usuario el nodo inicial
inicio = input(
    "\nIngrese el nodo inicial: "
).upper()

# Solicitar al usuario el nodo destino
destino = input(
    "Ingrese el nodo destino: "
).upper()

# Verificar que los nodos existan
if inicio not in grafo or destino not in grafo:

    print("\nError: nodo no válido.")

else:

    # Informar qué búsqueda realizará el programa
    print("\nSe buscará el camino mínimo")

    print(
        f"Desde {inicio} hasta {destino}"
    )

    # Ejecutar Dijkstra
    distancias, anteriores = dijkstra(
        grafo,
        inicio
    )

    # Reconstruir el camino mínimo
    camino = obtener_camino(
        anteriores,
        destino
    )

    # Mostrar una sección final con los resultados
    print("\n" + "=" * 50)

    # Título del resultado final
    print("RESULTADO FINAL")

    # Línea decorativa
    print("=" * 50)

    # Mostrar la secuencia de nodos
    # que forman el camino mínimo
    print(
        "\nCamino mínimo encontrado:"
    )

    # Mostrar el recorrido usando flechas
    print(
        " -> ".join(camino)
    )

    # Mostrar el costo total calculado
    # por el algoritmo
    print(
        "\nCosto total:",
        distancias[destino]
    )

    # Mostrar el grafo final
    mostrar_grafo(
        grafo,
        camino
    )