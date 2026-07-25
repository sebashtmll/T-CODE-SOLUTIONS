# pyrefly: ignore [missing-import]
import time
import os
# pyrefly: ignore [missing-import]
import matplotlib
matplotlib.use('Agg')
# pyrefly: ignore [missing-import]
import matplotlib.pyplot as plt
from tokens import lexer
from parser import parser

def procesar_archivo(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    
    start_time = time.perf_counter()
    lexer.input(data)
    ast = parser.parse(lexer=lexer)
    end_time = time.perf_counter()
    
    return end_time - start_time, ast

def medir_promedio(file_path, iteraciones=1000):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    
    start_time = time.perf_counter()
    for _ in range(iteraciones):
        lexer.input(data)
        _ = parser.parse(lexer=lexer)
    end_time = time.perf_counter()
    
    return (end_time - start_time) / iteraciones

def main():
    # Buscar todos los archivos del dataset en el mismo directorio que este script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    archivos = [os.path.join(base_dir, f) for f in os.listdir(base_dir) if f.startswith('docker_compose_dataset_') and f.endswith('.yml')]
    archivos.sort()
    
    if not archivos:
        print("No se encontraron archivos en el dataset.")
        return
        
    nombres = []
    tamanos = []
    tiempos = []
    
    print("-" * 80)
    print(f"{'Archivo':<45} | {'Tamaño (Bytes)':<15} | {'Tiempo Promedio (ms)':<20}")
    print("-" * 80)
    
    for path in archivos:
        f_name = os.path.basename(path)
        size_bytes = os.path.getsize(path)
        
        # Obtener el AST de una ejecución simple para verificar corrección
        _, ast = procesar_archivo(path)
        
        # Medir tiempo promedio estable con 1000 ejecuciones
        t_promedio = medir_promedio(path, iteraciones=1000)
        t_promedio_ms = t_promedio * 1000 # Convertir a milisegundos
        
        nombres.append(f_name.replace('docker_compose_dataset_compose_', 'C_'))
        tamanos.append(size_bytes)
        tiempos.append(t_promedio_ms)
        
        print(f"{f_name:<45} | {size_bytes:<15} | {t_promedio_ms:<20.4f}")
        print(f"AST Generado: {ast}\n")

    print("-" * 80)

    # Generar gráfico con matplotlib con un diseño premium y limpio
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Configurar estilo premium
    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
    ax1.grid(True, linestyle='--', alpha=0.6)
    
    # Ordenar los datos por tamaño de archivo para una curva de complejidad coherente
    datos_ordenados = sorted(zip(tamanos, tiempos, nombres), key=lambda x: x[0])
    tamanos_ord = [x[0] for x in datos_ordenados]
    tiempos_ord = [x[1] for x in datos_ordenados]
    nombres_ord = [x[2] for x in datos_ordenados]

    # Graficar Tamaño vs Tiempo
    color = '#1f77b4'
    ax1.set_xlabel('Tamaño del archivo (Bytes)', fontweight='bold', fontsize=12)
    ax1.set_ylabel('Tiempo de análisis (ms)', color=color, fontweight='bold', fontsize=12)
    line1 = ax1.plot(tamanos_ord, tiempos_ord, color=color, marker='o', linewidth=2, markersize=8, label='Tiempo de Parseo')
    ax1.tick_params(axis='y', labelcolor=color)

    # Añadir etiquetas con los nombres abreviados de los archivos en cada punto
    for i, txt in enumerate(nombres_ord):
        ax1.annotate(txt, (tamanos_ord[i], tiempos_ord[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9, fontweight='bold')

    plt.title('Rendimiento del Analizador de Docker Compose (PLY)\nTamaño de Archivo vs. Tiempo de Parseo', fontsize=14, fontweight='bold', pad=15)
    
    # Guardar gráfico en disco
    output_image = os.path.join(base_dir, 'grafico_tiempos.png')
    plt.tight_layout()
    plt.savefig(output_image, dpi=300)
    print(f"Gráfico de rendimiento guardado como: {output_image}")
    plt.close()

if __name__ == '__main__':
    main()