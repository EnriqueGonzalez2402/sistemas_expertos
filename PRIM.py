import heapq

def prim_complejo(grafo):
    if not grafo:
        raise ValueError("El grafo está vacío")

    inicio = list(grafo.keys())[0]

    visitados = set([inicio])
    aristas_mst = []
    costo_total = 0

    cola = []

    # Insertamos todas las aristas del nodo inicial
    for vecino, peso in grafo[inicio].items():
        heapq.heappush(cola, (peso, inicio, vecino))

    while cola:
        peso, origen, destino = heapq.heappop(cola)

        if destino not in visitados:
            visitados.add(destino)
            aristas_mst.append((origen, destino, peso))
            costo_total += peso

            print(f"Agregando arista {origen} - {destino} con costo {peso}")

            for vecino, costo in grafo[destino].items():
                if vecino not in visitados:
                    heapq.heappush(cola, (costo, destino, vecino))

    # Verificar si el grafo es conexo
    if len(visitados) != len(grafo):
        raise ValueError("El grafo no es conexo")

    return aristas_mst, costo_total


grafo_red = {
    "Nodo1": {"Nodo2": 4, "Nodo3": 3},
    "Nodo2": {"Nodo1": 4, "Nodo3": 1, "Nodo4": 2},
    "Nodo3": {"Nodo1": 3, "Nodo2": 1, "Nodo4": 5},
    "Nodo4": {"Nodo2": 2, "Nodo3": 5, "Nodo5": 7},
    "Nodo5": {"Nodo4": 7}
}

aristas, costo = prim_complejo(grafo_red)

print("\nÁrbol de expansión mínima:")
for a in aristas:
    print(a)

print("Costo total:", costo)