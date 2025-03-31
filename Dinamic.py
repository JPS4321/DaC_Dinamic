import random
import itertools
import time

def generar_grafo(n, rango=(1, 30)):
    grafo = {}
    for i in range(n):
        grafo[i] = {}
        for j in range(n):
            grafo[i][j] = 0 if i == j else random.randint(*rango)
    return grafo

def imprimir_grafo(grafo):
    print("Grafo generado:")
    for nodo in grafo:
        print(f"{nodo} -> {grafo[nodo]}")

def tsp_dp(grafo, inicio):
    n = len(grafo)
    memo = [[float('inf')] * n for _ in range(1 << n)]
    memo[1 << inicio][inicio] = 0

    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                next_mask = mask | (1 << v)
                memo[next_mask][v] = min(
                    memo[next_mask][v],
                    memo[mask][u] + grafo[u][v]
                )

    # Regresar al nodo de inicio
    min_cost = float('inf')
    last_node = -1
    full_mask = (1 << n) - 1
    for i in range(n):
        cost = memo[full_mask][i] + grafo[i][inicio]
        if cost < min_cost:
            min_cost = cost
            last_node = i

    # Reconstrucción de la ruta
    ruta = [inicio]
    mask = full_mask
    curr = last_node
    while mask != (1 << inicio):
        ruta.append(curr)
        prev = -1
        for i in range(n):
            if i != curr and (mask & (1 << i)):
                if memo[mask][curr] == memo[mask ^ (1 << curr)][i] + grafo[i][curr]:
                    prev = i
                    break
        mask ^= (1 << curr)
        curr = prev
    ruta.append(inicio)
    ruta.reverse()

    return ruta, min_cost

# --- CONFIGURACIÓN ---
n = 22             
inicio = 1           
grafo = generar_grafo(n)
imprimir_grafo(grafo)

# --- RESOLVER ---
inicio_tiempo = time.perf_counter()
ruta, costo = tsp_dp(grafo, inicio)
fin_tiempo = time.perf_counter()


print(f"Ruta óptima iniciando en el nodo {inicio}:", ruta)
print("Costo total:", costo)
print("Tiempo de ejecución (DP):", fin_tiempo - inicio_tiempo, "segundos")
