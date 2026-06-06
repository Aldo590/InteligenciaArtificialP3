# Librería para trabajar con grafos
# Instalar: pip install networkx matplotlib
import networkx as nx

# Librería para crear gráficos
import matplotlib.pyplot as plt


# Buscar a qué conjunto pertenece un nodo
def find(padre, nodo):

    # Si el nodo es su propio padre,
    # ya se encontró la raíz del conjunto
    if padre[nodo] == nodo:

        return nodo

    # Buscar recursivamente la raíz
    return find(padre, padre[nodo])


# Unir dos conjuntos diferentes
def union(padre, nodo1, nodo2):

    # Obtener la raíz del primer nodo
    raiz1 = find(padre, nodo1)

    # Obtener la raíz del segundo nodo
    raiz2 = find(padre, nodo2)

    # Hacer que un conjunto apunte al otro
    padre[raiz2] = raiz1


# Algoritmo de Kruskal
def kruskal(grafo, tipo="min"):

    # Lista donde se almacenarán
    # las aristas del árbol resultante
    arbol = []

    # Costo total acumulado
    costo_total = 0

    # Lista con todas las aristas
    aristas = []

    # Conjunto para evitar duplicados
    agregadas = set()

    # Recorrer todas las conexiones del grafo
    for origen in grafo:

        for destino, peso in grafo[origen].items():

            # Crear una representación única
            # de la arista
            arista = tuple(
                sorted([origen, destino])
            )

            # Si la arista ya fue agregada,
            # ignorarla
            if arista in agregadas:

                continue

            # Registrar la arista como agregada
            agregadas.add(arista)

            # Guardar origen, destino y peso
            aristas.append(
                (origen, destino, peso)
            )

    # Ordenar aristas según la opción elegida
    if tipo == "min":

        # Orden ascendente para mínimo coste
        aristas.sort(
            key=lambda x: x[2]
        )

    else:

        # Orden descendente para máximo coste
        aristas.sort(
            key=lambda x: x[2],
            reverse=True
        )

    # Crear conjuntos iniciales
    padre = {}

    for nodo in grafo:

        # Cada nodo inicia en su propio conjunto
        padre[nodo] = nodo

    # Contador para las iteraciones
    paso = 1

    # Recorrer todas las aristas ordenadas
    for origen, destino, peso in aristas:

        # Mostrar un encabezado para separar
        # visualmente cada iteración
        print("\n" + "=" * 50)

        # Mostrar el número de paso actual
        print("PASO", paso)

        # Línea decorativa
        print("=" * 50)

        # Mostrar cuál es la arista
        # que se está evaluando
        print("\nArista evaluada:")

        print(
            f"{origen} -- {destino}"
        )

        # Mostrar el peso de la arista
        print(
            f"\nPeso: {peso}"
        )

        # Obtener el conjunto al que
        # pertenece el nodo origen
        raiz1 = find(
            padre,
            origen
        )

        # Obtener el conjunto al que
        # pertenece el nodo destino
        raiz2 = find(
            padre,
            destino
        )

        # Si las raíces son distintas
        # no se formará un ciclo
        if raiz1 != raiz2:

            # Informar que la arista es válida
            print(
                "\nNo forma ciclo."
            )

            # Informar que será agregada
            print(
                "Se agrega al árbol."
            )

            # Agregar la arista al árbol
            arbol.append(
                (origen, destino, peso)
            )

            # Unir ambos conjuntos
            union(
                padre,
                origen,
                destino
            )

            # Sumar el peso al costo total
            costo_total += peso

        else:

            # Informar que la arista
            # produciría un ciclo
            print(
                "\nForma un ciclo."
            )

            # Informar que no será agregada
            print(
                "No se agrega."
            )

        # Mostrar el costo acumulado
        # hasta este momento
        print(
            f"\nCosto acumulado: "
            f"{costo_total}"
        )

        # Mostrar las aristas que ya
        # forman parte del árbol
        print(
            "\nAristas seleccionadas:"
        )

        for o, d, p in arbol:

            print(
                f"{o} -- {d} "
                f"(peso {p})"
            )

        # Si ya se tienen N-1 aristas,
        # el árbol está completo
        if len(arbol) == len(grafo) - 1:

            break

        # Avanzar al siguiente paso
        paso += 1

    # Regresar árbol y costo total
    return arbol, costo_total


# Mostrar el árbol gráficamente
def mostrar_grafo(grafo, arbol, titulo):

    # Crear estructura compatible
    # con NetworkX
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

    # Calcular posiciones automáticas
    # para los nodos
    pos = nx.spring_layout(
        G,
        seed=42
    )

    # Lista para almacenar únicamente
    # las aristas del árbol
    arbol_aristas = []

    # Extraer origen y destino
    # de cada arista seleccionada
    for origen, destino, peso in arbol:

        arbol_aristas.append(
            (origen, destino)
        )

    # Dibujar todos los nodos
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=2000
    )

    # Dibujar todas las aristas
    # originales en gris
    nx.draw_networkx_edges(
        G,
        pos,
        edge_color="gray",
        width=2
    )

    # Resaltar las aristas que forman
    # parte del árbol encontrado
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=arbol_aristas,
        edge_color="red",
        width=4
    )

    # Obtener los pesos
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

    # Mostrar un título descriptivo
    plt.title(titulo)

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

# Mostrar el título principal
print("SIMULADOR DE KRUSKAL")

# Mostrar las opciones disponibles
print("\n1. Árbol de mínimo coste")
print("2. Árbol de máximo coste")

# Solicitar al usuario el tipo
# de árbol que desea construir
opcion = input(
    "\nSeleccione una opción: "
)

# Verificar si se eligió
# mínimo coste
if opcion == "1":

    # Informar qué algoritmo
    # se ejecutará
    print(
        "\nConstruyendo árbol de mínimo coste..."
    )

    # Ejecutar Kruskal mínimo
    arbol, costo_total = kruskal(
        grafo,
        "min"
    )

    # Título de la gráfica
    titulo = (
        "Arbol de Minimo Coste - Kruskal"
    )

# Verificar si se eligió
# máximo coste
elif opcion == "2":

    # Informar qué algoritmo
    # se ejecutará
    print(
        "\nConstruyendo árbol de máximo coste..."
    )

    # Ejecutar Kruskal máximo
    arbol, costo_total = kruskal(
        grafo,
        "max"
    )

    # Título de la gráfica
    titulo = (
        "Arbol de Maximo Coste - Kruskal"
    )

else:

    # Informar que la opción
    # capturada no es válida
    print("\nOpción no válida.")

    exit()

# Mostrar encabezado de resultados
print("\n" + "=" * 50)

# Mostrar título de la sección final
print("RESULTADO FINAL")

# Línea decorativa
print("=" * 50)

# Mostrar las aristas que forman
# el árbol encontrado
print("\nAristas seleccionadas:")

for origen, destino, peso in arbol:

    print(
        f"{origen} -- {destino} "
        f"(peso {peso})"
    )

# Mostrar el costo total
# del árbol resultante
print(
    f"\nCosto total: "
    f"{costo_total}"
)

# Mostrar la gráfica final
mostrar_grafo(
    grafo,
    arbol,
    titulo
)