# Estuctura de codigo con algoritmo de dickstra

def conseguir_ruta(dest, predecesores):
    ruta = []
    nodo_actual = dest
    while nodo_actual is not None:
        ruta.insert(0, nodo_actual)  # inserta el nodo al inicio de la ruta
        nodo_actual = predecesores[nodo_actual]  # actualiza el nodo actual al predecesor
    return ruta

def siguiente_nodo(distancias, visitados):
    nodo_siguiente = None
    distancia_minima = float('inf')
    for nodo in distancias:
        if nodo not in visitados and distancias[nodo] < distancia_minima:
            distancia_minima = distancias[nodo]
            nodo_siguiente = nodo
    return nodo_siguiente

def dijkstra(grafo, inicio, destino):
    distancias = {}
    predecesores = {}
    visitados = []

    for nodo in grafo:
        distancias[nodo] = float('inf')  # inicia todas las distancias como infinito
        predecesores[nodo] = None  # inicializa todos los predecesores como None

    distancias[inicio] = 0  # la distancia al nodo de inicio es 0

    while True:
        nodo_actual = siguiente_nodo(distancias, visitados)  # obtiene el siguiente nodo no visitado con la distancia más corta
        if nodo_actual is None:  # si no hay más nodos por visitar, termina el algoritmo
            break
        if nodo_actual == destino:  # si se ha llegado al destino, termina el algoritmo
            break

        visitados.append(nodo_actual)  # marca el nodo actual como visitado

        for vecino in grafo[nodo_actual]:  # recorre los vecinos del nodo actual
            peso, nodo_vecino = vecino
            if nodo_vecino not in visitados:  # si el vecino no ha sido visitado
                nueva_distancia = distancias[nodo_actual] + peso  # calcula la nueva distancia al vecino a través del nodo actual
                if nueva_distancia < distancias[nodo_vecino]:  # si la nueva distancia es menor que la distancia conocida
                    distancias[nodo_vecino] = nueva_distancia  # actualiza la distancia al vecino
                    predecesores[nodo_vecino] = nodo_actual  # actualiza el predecesor del vecino

    ruta = conseguir_ruta(destino, predecesores)  # obtiene la ruta desde el destino hasta el inicio usando los predecesores
    if distancias[destino] == float('inf'):  # si la distancia al destino es infinito, significa que no hay ruta
        return [], float('inf')
    else:
        return ruta, distancias[destino]
    