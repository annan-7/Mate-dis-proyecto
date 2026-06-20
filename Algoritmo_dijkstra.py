# Estuctura de codigo con algoritmo de dickstra
def dijkstra(graph, inicio, destino):
    # incializa las distancias y predecesores
    distancias = {nodo: float('inf') for nodo in graph}
    predecesores = {nodo: None for nodo in graph}
    distancias[inicio] = 0

    # Conjunto de nodos no visitados
    no_visitados = set(graph.keys())

    while no_visitados:
        # Selecciona el nodo con la distancia mínima
        nodo_actual = min(no_visitados, key=lambda nodo: distancias[nodo])

        # Si el nodo actual es el destino ya se encontro el camino mas corto
        if nodo_actual == destino:
            break

        no_visitados.remove(nodo_actual)

        # Actualiza las distancias
        for peso, vecino in graph[nodo_actual]:
            if vecino in no_visitados:
                nueva_distancia = distancias[nodo_actual] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual

    # reconstruye el camino desde el destino hasta el inicio
    camino = []
    nodo = destino
    while nodo is not None:
        camino.append(nodo)
        nodo = predecesores[nodo]
    camino.reverse()

    return camino, distancias[destino] if distancias[destino] != float('inf') else None
