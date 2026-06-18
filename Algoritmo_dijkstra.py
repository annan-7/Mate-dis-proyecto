# Estuctura de codigo con algoritmo de dickstra
import heapq


def dijkstra(grafo, inicio, destino):
    # Inicializar la cola de prioridad y las distancias
    cola_prioridad = [(0, inicio)]  # (distancia, nodo)
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    predecesores = {nodo: None for nodo in grafo}

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad) # heappop lo que hace es q siempre devuelve el nodo con la menor distancia

        # Si hemos llegado al destino, reconstruimos el camino
        if nodo_actual == destino:
            camino = []
            while nodo_actual is not None:
                camino.append(nodo_actual)
                nodo_actual = predecesores[nodo_actual]
            return camino[::-1], distancias[destino]

        # Si la distancia actual es mayor que la registrada, ignoramos este nodo
        if distancia_actual > distancias[nodo_actual]:
            continue

        # Explorar los vecinos del nodo actual
        for peso, vecino in grafo[nodo_actual]:
            distancia_nueva = distancia_actual + peso

            if distancia_nueva < distancias[vecino]:
                distancias[vecino] = distancia_nueva
                predecesores[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (distancia_nueva, vecino)) # heappush agrega un nuevo nodo a la cola de prioridad con su distancia actualizada

    return None, float('inf')  # Si no hay camino entre inicio y destino
