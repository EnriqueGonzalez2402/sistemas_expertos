import heapq

class Grafo:
    def __init__(self):
        # Diccionario de adyacencia
        self.vertices = {}

    def agregar_arista(self, origen, destino, peso):
        """
        Agrega una arista bidireccional
        """
        if peso < 0:
            raise ValueError("Dijkstra no permite pesos negativos")

        if origen not in self.vertices:
            self.vertices[origen] = {}
        if destino not in self.vertices:
            self.vertices[destino] = {}

        self.vertices[origen][destino] = peso
        self.vertices[destino][origen] = peso


def dijkstra(grafo, inicio):
    if inicio not in grafo.vertices:
        raise ValueError("El nodo inicial no existe en el grafo")

    distancias = {v: float('inf') for v in grafo.vertices}
    anterior = {v: None for v in grafo.vertices}
    visitados = set()

    distancias[inicio] = 0

    # Cola de prioridad (distancia acumulada, nodo)
    cola = [(0, inicio)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        # Si ya fue procesado, lo ignoramos
        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)

        print(f"Procesando nodo: {nodo_actual} con distancia {distancia_actual}")

        for vecino, peso in grafo.vertices[nodo_actual].items():
            if vecino not in visitados:
                nueva_dist = distancia_actual + peso

                if nueva_dist < distancias[vecino]:
                    distancias[vecino] = nueva_dist
                    anterior[vecino] = nodo_actual
                    heapq.heappush(cola, (nueva_dist, vecino))

    return distancias, anterior


def reconstruir_ruta(anterior, destino):
    ruta = []
    while destino is not None:
        ruta.append(destino)
        destino = anterior[destino]
    return list(reversed(ruta))


# -------------------- EJECUCIÓN --------------------

g = Grafo()

g.agregar_arista("Almacen", "A", 5)
g.agregar_arista("Almacen", "B", 2)
g.agregar_arista("A", "C", 4)
g.agregar_arista("B", "C", 1)
g.agregar_arista("B", "D", 7)
g.agregar_arista("C", "D", 3)
g.agregar_arista("C", "EntregaFinal", 6)
g.agregar_arista("D", "EntregaFinal", 2)

distancias, anterior = dijkstra(g, "Almacen")

print("\nDistancias finales:")
for nodo in distancias:
    print(nodo, "->", distancias[nodo])

print("\nRuta óptima a EntregaFinal:")
print(reconstruir_ruta(anterior, "EntregaFinal"))