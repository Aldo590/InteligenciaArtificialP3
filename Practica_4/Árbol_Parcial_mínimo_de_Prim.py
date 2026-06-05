# Librería para trabajar con grafos
# Instalar: pip install networkx matplotlib
import networkx as nx

# Librería para crear y mostrar gráficos
import matplotlib.pyplot as plt


# Algoritmo de Prim
def prim(grafo, inicio):

    # Conjunto que almacena los nodos
    # que ya forman parte del árbol
    visitados = {inicio}

    # Lista donde se guardarán las aristas
    # seleccionadas para el árbol mínimo
    arbol = []

    # Costo total acumulado del árbol
    costo_total = 0

    # Contador para mostrar las iteraciones
    paso = 1

    # Continuar hasta que todos los nodos
    # formen parte del árbol
    while len(visitados) < len(grafo):

        # Guardará la mejor arista encontrada
        mejor_arista = None

        # Peso mínimo encontrado en esta iteración
        peso_minimo = float("inf")

        # Revisar todos los nodos que ya están
        # dentro del árbol
        for origen in visitados:

            # Revisar todas las conexiones
            # del nodo actual
            for destino, peso in grafo[origen].items():

                # Si el nodo destino ya está
                # en el árbol, ignorarlo
                if destino in visitados:

                    continue

                # Si encontramos una arista
                # con menor peso, guardarla
                if peso < peso_minimo:

                    peso_minimo = peso

                    mejor_arista = (
                        origen,
                        destino,
                        peso
                    )

        # Si no se encontró una arista válida
        # significa que el grafo no está conectado
        if mejor_arista is None:

            break

        # Separar los datos de la arista elegida
        origen, destino, peso = mejor_arista

        # Agregar el nuevo nodo al conjunto
        # de nodos visitados
        visitados.add(destino)

        # Guardar la arista dentro del árbol
        arbol.append(
            (origen, destino, peso)
        )

        # Sumar el peso al costo total
        costo_total += peso

        # Mostrar un encabezado para separar
        # visualmente cada iteración
        print("\n" + "=" * 50)

        # Mostrar número de paso
        print("PASO", paso)

        print("=" * 50)

        # Mostrar la arista seleccionada
        print(
            "\nArista seleccionada:"
        )

        print(
            f"{origen} -- {destino}"
        )

        # Mostrar el peso de la arista
        print(
            f"\nPeso de la arista: {peso}"
        )

        # Mostrar el costo acumulado
        # del árbol hasta este momento
        print(
            f"\nCosto acumulado: "
            f"{costo_total}"
        )

        # Mostrar qué nodos ya forman
        # parte del árbol mínimo
        print(
            "\nNodos dentro del árbol:"
        )

        print(
            sorted(visitados)
        )

        # Mostrar las aristas que ya
        # pertenecen al árbol
        print(
            "\nAristas del árbol hasta ahora:"
        )

        for o, d, p in arbol:

            print(
                f"{o} -- {d} "
                f"(peso {p})"
            )

        # Pasar a la siguiente iteración
        paso += 1

    # Regresar el árbol y el costo total
    return arbol, costo_total


# Mostrar gráficamente el árbol mínimo
def mostrar_grafo(grafo, arbol):

    # Crear una estructura de grafo
    # compatible con NetworkX
    G = nx.Graph()

    # Agregar todas las conexiones
    # del grafo original
    for origen in grafo:

        for destino, peso in grafo[origen].items():

            G.add_edge(
                origen,
                destino,
                weight=peso
            )

    # Calcular automáticamente la posición
    # de cada nodo en la ventana
    pos = nx.spring_layout(
        G,
        seed=42
    )

    # Lista que almacenará únicamente
    # las aristas pertenecientes al MST
    mst_edges = []

    # Extraer las conexiones del árbol
    for origen, destino, peso in arbol:

        mst_edges.append(
            (origen, destino)
        )

    # Dibujar todos los nodos
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000
    )

    # Dibujar todas las conexiones
    # originales en color gris
    nx.draw_networkx_edges(
        G,
        pos,
        edge_color="gray",
        width=2
    )

    # Resaltar las conexiones que
    # pertenecen al árbol mínimo
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=mst_edges,
        edge_color="red",
        width=4
    )

    # Obtener los pesos de las conexiones
    etiquetas = nx.get_edge_attributes(
        G,
        "weight"
    )

    # Mostrar los pesos sobre las aristas
    nx.draw_networkx_edge_labels(
        G,
        pos,
        edge_labels=etiquetas
    )

    # Título de la ventana
    plt.title(
        "Arbol Parcial Minimo de Prim"
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

# Solicitar el nodo desde el que
# comenzará el algoritmo
inicio = input(
    "\nIngrese el nodo inicial: "
).upper()

# Verificar que el nodo exista
if inicio not in grafo:

    print("\nError: nodo no válido.")

else:

    # Informar al usuario que comenzará
    # la construcción del árbol mínimo
    print(
        "\nConstruyendo Árbol Parcial Mínimo..."
    )

    # Ejecutar el algoritmo de Prim
    arbol, costo_total = prim(
        grafo,
        inicio
    )

    # Mostrar encabezado del resultado final
    print("\n" + "=" * 50)

    print("RESULTADO FINAL")

    print("=" * 50)

    # Mostrar todas las aristas
    # que forman el árbol mínimo
    print(
        "\nAristas del árbol:"
    )

    for origen, destino, peso in arbol:

        print(
            f"{origen} -- {destino} "
            f"(peso {peso})"
        )

    # Mostrar el costo total del árbol
    print(
        "\nCosto total:",
        costo_total
    )

    # Mostrar la gráfica final
    mostrar_grafo(
        grafo,
        arbol
    )