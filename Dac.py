import random
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

def distancia_total(grafo, ruta):
    return sum(grafo[ruta[i]][ruta[i+1]] for i in range(len(ruta)-1)) + grafo[ruta[-1]][ruta[0]]

def merge_rutas(grafo, r1, r2):
    mejor_ruta = []
    mejor_costo = float('inf')
    for i in range(len(r1)):
        for j in range(len(r2)):
            nueva = r1[i:] + r1[:i] + r2[j:] + r2[:j]
            costo = distancia_total(grafo, nueva)
            if costo < mejor_costo:
                mejor_costo = costo
                mejor_ruta = nueva
    return mejor_ruta

def tsp_dac_aproximado(grafo, nodos):
    if len(nodos) <= 3:
        return nodos
    mid = len(nodos) // 2
    izquierda = tsp_dac_aproximado(grafo, nodos[:mid])
    derecha = tsp_dac_aproximado(grafo, nodos[mid:])
    return merge_rutas(grafo, izquierda, derecha)

# --- CONFIGURACIÓN ---
random.seed(0)                     # Para resultados consistentes
n = 10                            # Número de nodos
inicio = 1                         # Nodo inicial deseado (0 a n-1)
grafo = generar_grafo(n)
imprimir_grafo(grafo)

nodos = list(grafo.keys())
nodos.remove(inicio)
nodos = [inicio] + nodos          

# --- EJECUCIÓN ÚNICA ---
inicio_tiempo = time.perf_counter()
ruta_aprox = tsp_dac_aproximado(grafo, nodos)
costo_aprox = distancia_total(grafo, ruta_aprox)
fin_tiempo = time.perf_counter()

print(f"Ruta aproximada iniciando en el nodo {inicio}:", ruta_aprox)
print("Costo total:", costo_aprox)
print("Tiempo de ejecución (DaC):", fin_tiempo - inicio_tiempo, "segundos")
