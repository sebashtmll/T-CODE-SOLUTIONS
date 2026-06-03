import time
import math

n = 200
a = [1.0] * n
b = [-5.0] * n
c = [6.0] * n
resultados = [(0.0, 0.0)] * n

inicio = time.perf_counter()

for i in range(n):
    disc = b[i] * b[i] - 4.0 * a[i] * c[i]
    x1 = (-b[i] + math.sqrt(disc)) / (2.0 * a[i])
    x2 = (-b[i] - math.sqrt(disc)) / (2.0 * a[i])
    resultados[i] = (x1, x2)

fin = time.perf_counter()
tiempo_ms = (fin - inicio) * 1000

print(f"Python - Tiempo de cálculo: {tiempo_ms:.4f} ms")
print(f"Control (Último resultado): x1 = {resultados[-1][0]}, x2 = {resultados[-1][1]}")