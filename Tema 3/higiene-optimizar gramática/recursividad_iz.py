# recursividad_iz.py
"""
CASO (b): RECURSIVIDAD POR LA IZQUIERDA
========================================
Naturaleza: Defecto ESTRUCTURAL de la gramatica.

PROBLEMA REAL:
    Un parser descendente (top-down) al intentar procesar la regla
    E -> E + T entra en un BUCLE INFINITO porque expande E sin consumir entrada.
    
    NO ES POSIBLE "ejecutar" este ejemplo sin que el programa se congele.
    
SOLUCION EN ESTE CODIGO:
    Se demuestra la patologia mediante la APLICACION DEL ALGORITMO
    de eliminacion de recursividad por izquierda, mostrando PASO A PASO
    como transformar la gramatica original en una equivalente sin el defecto.
"""

def mostrar_seccion(titulo):
    print("\n" + "=" * 70)
    print(f" {titulo}")
    print("=" * 70)

def mostrar_paso(numero, titulo):
    print(f"\n[PASO {numero}] {titulo}")
    print("-" * 50)

def main():
    print("\n" + "*" * 70)
    print(" " * 18 + "RECURSIVIDAD POR LA IZQUIERDA")
    print(" " * 12 + "Demostracion del Algoritmo de Eliminacion")
    print("*" * 70)
    
    # ============================================================
    # EXPLICACION DEL PROBLEMA
    # ============================================================
    mostrar_seccion("¿QUE ES LA RECURSIVIDAD POR LA IZQUIERDA?")
    print("""
    Una produccion es recursiva por izquierda cuando el simbolo no terminal
    de la izquierda aparece como el PRIMER simbolo de su propio cuerpo.
    
    EJEMPLO:
        E -> E + T | T
        ^    ^
        |    |
        |    +-- El primer simbolo despues de -> es E (el mismo)
        |
        +-- Simbolo no terminal de la izquierda
    
    ¿POR QUE ES UN PROBLEMA?
        Un parser descendente (top-down) intentara expandir E.
        Para expandir E, necesita expandir E NUEVAMENTE.
        Esto se repite sin consumir NINGUN token de entrada.
        RESULTADO: BUCLE INFINITO (el programa se congela).
    
    NOTA: Este defecto NO puede demostrarse ejecutandolo,
          porque el programa nunca terminaria.
    """)
    
    input("\nPresione Enter para continuar con la demostracion...")
    
    # ============================================================
    # GRAMATICA ORIGINAL
    # ============================================================
    mostrar_seccion("GRAMATICA ORIGINAL (CON EL DEFECTO)")
    print("""
    En notacion BNF:
        <E> -> <E> + <T> | <T>
        <T> -> id | numero
    
    Produccion problematica: <E> -> <E> + <T>
    """)
    
    input("\nPresione Enter para aplicar el algoritmo...")
    
    # ============================================================
    # PASO 1: IDENTIFICAR COMPONENTES
    # ============================================================
    mostrar_paso(1, "Identificar componentes segun la formula A -> Aα | β")
    print("""
    Formula general:
        A -> Aα | β
    
    Donde:
        A  = es el no terminal recursivo
        α  = es la secuencia que sigue despues de A (parte recursiva)
        β  = es la alternativa que NO empieza con A
    
    Aplicando a nuestro ejemplo:
        A = E
        α = + T      (lo que sigue despues de la recursion)
        β = T        (alternativa que NO empieza con E)
    """)
    
    input("Presione Enter para continuar...")
    
    # ============================================================
    # PASO 2: APLICAR TRANSFORMACION
    # ============================================================
    mostrar_paso(2, "Aplicar el algoritmo de transformacion")
    print("""
    El algoritmo (Aho, Sethi & Ullman) establece:
    
        Dada:  A -> Aα | β
        Se transforma en:
               A -> β A'
               A' -> α A' | ε
    
    Donde A' es un NUEVO no terminal (no existia antes).
    ε representa la cadena vacia.
    
    Sustituyendo nuestros valores (A=E, α=+T, β=T):
    
        E -> T E'
        E' -> + T E' | ε
    """)
    
    input("Presione Enter para continuar...")
    
    # ============================================================
    # PASO 3: GRAMATICA TRANSFORMADA
    # ============================================================
    mostrar_paso(3, "Gramatica resultante (SIN recursividad izquierda)")
    print("""
    GRAMATICA TRANSFORMADA:
        <E>  -> <T> <E'>
        <E'> -> + <T> <E'> | ε
        <T>  -> id | numero
    
    VERIFICACION:
        ¿Hay recursividad por izquierda?
            E -> T E'     → El primer simbolo es T (NO es E) ✓
            E' -> + T E'  → El primer simbolo es + (NO es E') ✓
            E' -> ε       → Produccion vacia para terminar ✓
        
        La recursividad ahora es POR LA DERECHA, que es segura
        para parsers descendentes (top-down).
    """)
    
    # ============================================================
    # CONCLUSION
    # ============================================================
    mostrar_seccion("CONCLUSION")
    print("""
    La recursividad por la izquierda es un DEFECTO ESTRUCTURAL que:
        1. Impide el uso de parsers descendentes (top-down)
        2. Causa bucles infinitos en el analisis sintactico
        3. Debe ser eliminada mediante el algoritmo mostrado
    
    La gramatica transformada es EQUIVALENTE a la original
    (reconoce el mismo lenguaje) pero es PROCESABLE por un parser.
    
    [OK] Demostracion completada.
    """)
    
    print("\n" + "=" * 70)
    print(" " * 22 + "FIN DE LA DEMOSTRACION")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()