class UnionFind:
    def __init__(self, nodos):
        self.padre = {n: n for n in nodos}
        self.rango = {n: 0 for n in nodos}

    def encontrar(self, nodo):
        if self.padre[nodo] != nodo:
            self.padre[nodo] = self.encontrar(self.padre[nodo])
        return self.padre[nodo]

    def unir(self, nodo1, nodo2):
        raiz1 = self.encontrar(nodo1)
        raiz2 = self.encontrar(nodo2)

        if raiz1 == raiz2:
            return False

        if self.rango[raiz1] < self.rango[raiz2]:
            self.padre[raiz1] = raiz2
        else:
            self.padre[raiz2] = raiz1
            if self.rango[raiz1] == self.rango[raiz2]:
                self.rango[raiz1] += 1

        return True


def kruskal_complejo(grafo):
    aristas = []

    # Evitar duplicados en grafo no dirigido
    vistos = set()
    for nodo in grafo:
        for vecino, peso in grafo[nodo].items():
            if (vecino, nodo) not in vistos:
                aristas.append((peso, nodo, vecino))
                vistos.add((nodo, vecino))

    aristas.sort()

    uf = UnionFind(grafo.keys())

    mst = []
    costo_total = 0

    for peso, nodo1, nodo2 in aristas:
        if uf.unir(nodo1, nodo2):
            mst.append((nodo1, nodo2, peso))
            costo_total += peso
            print(f"Conectando {nodo1} - {nodo2} costo {peso}")

    if len(mst) != len(grafo) - 1:
        raise ValueError("El grafo no es conexo")

    return mst, costo_total


grafo_ciudades = {
    "A": {"B": 6, "C": 1, "D": 5},
    "B": {"A": 6, "C": 5, "E": 3},
    "C": {"A": 1, "B": 5, "D": 5, "E": 6},
    "D": {"A": 5, "C": 5, "E": 2},
    "E": {"B": 3, "C": 6, "D": 2}
}

mst, costo = kruskal_complejo(grafo_ciudades)

print("\nMST final:")
for a in mst:
    print(a)

print("Costo total mínimo:", costo)