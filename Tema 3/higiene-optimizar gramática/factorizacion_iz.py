# factorizacion_iz.py
"""
CASO (c): FACTORIZACION POR LA IZQUIERDA
=========================================
Naturaleza: Conflicto de DECISION del parser (problema de diseño).

PROBLEMA REAL:
    Un parser predictivo (LL(1)) al leer el prefijo comun "if (Cond) then Stmt"
    NO PUEDE DECIDIR si la produccion termina ahi o si viene "else Stmt".
    
    NO ES POSIBLE "ejecutar" este conflicto porque es un problema
    de DISEÑO DE LA GRAMATICA, no de ejecucion.
    
SOLUCION EN ESTE CODIGO:
    Se demuestra la patologia mostrando la GRAMATICA ORIGINAL CONFLICTIVA
    y la GRAMATICA OPTIMIZADA mediante FACTORIZACION.
"""

def mostrar_seccion(titulo):
    print("\n" + "=" * 70)
    print(f" {titulo}")
    print("=" * 70)

def mostrar_gramatica(titulo, producciones):
    print(f"\n[{titulo}]:")
    for nt, prods in producciones.items():
        for p in prods:
            print(f"   {nt} -> {' '.join(p)}")

def main():
    print("\n" + "*" * 70)
    print(" " * 15 + "FACTORIZACION POR LA IZQUIERDA")
    print(" " * 10 + "Demostracion del Problema del 'Else Colgante'")
    print("*" * 70)
    
    # ============================================================
    # EXPLICACION DEL PROBLEMA
    # ============================================================
    mostrar_seccion("¿QUE ES LA FACTORIZACION POR LA IZQUIERDA?")
    print("""
    Ocurre cuando dos o mas producciones del mismo no terminal
    comparten un PREFIJO COMUN extenso.
    
    EJEMPLO CLASICO (problema del 'else colgante' o dangling-else):
        Stmt -> if (Cond) then Stmt
              | if (Cond) then Stmt else Stmt
              | a
    
    Las dos primeras producciones comparten el prefijo:
        'if (Cond) then Stmt'
    
    ¿POR QUE ES UN PROBLEMA?
        Un parser LL(1) (predictivo) solo puede mirar UN token adelante.
        Cuando lee 'if (Cond) then Stmt', NO SABE si:
            - La produccion termina ahi (sin else)
            - O si debe esperar un 'else Stmt'
        
        El parser no puede decidir DETERMINISTICAMENTE.
    
    NOTA: Este conflicto NO puede demostrarse ejecutandolo,
          es un problema de DISEÑO DE LA GRAMATICA.
    """)
    
    input("\nPresione Enter para ver la gramatica original...")
    
    # ============================================================
    # GRAMATICA ORIGINAL CONFLICTIVA
    # ============================================================
    mostrar_seccion("GRAMATICA ORIGINAL (CONFLICTIVA)")
    
    gram_original = {
        "Stmt": [
            ["if", "(", "Cond", ")", "then", "Stmt"],
            ["if", "(", "Cond", ")", "then", "Stmt", "else", "Stmt"],
            ["a"]
        ],
        "Cond": [["x>0"]]
    }
    
    mostrar_gramatica("Gramatica original", gram_original)
    
    print("""
    [PROBLEMA IDENTIFICADO]:
        Las dos primeras producciones de Stmt comparten el prefijo:
            'if ( Cond ) then Stmt'
        
        Un parser LL(1) NO puede decidir que regla aplicar.
    """)
    
    input("\nPresione Enter para aplicar factorizacion...")
    
    # ============================================================
    # APLICAR FACTORIZACION
    # ============================================================
    mostrar_seccion("APLICANDO EL ALGORITMO DE FACTORIZACION")
    print("""
    ALGORITMO:
        Dadas producciones: A -> αβ1 | αβ2
        Se transforman en:   A -> α A'
                             A' -> β1 | β2
    
    APLICACION A NUESTRO EJEMPLO:
        A   = Stmt
        α   = if ( Cond ) then Stmt   (prefijo comun)
        β1  = ε                        (primera produccion termina)
        β2  = else Stmt                (segunda produccion continua)
    
    RESULTADO:
        Stmt    -> if ( Cond ) then Stmt OptElse | a
        OptElse -> else Stmt | ε
    """)
    
    input("Presione Enter para ver la gramatica optimizada...")
    
    # ============================================================
    # GRAMATICA OPTIMIZADA
    # ============================================================
    mostrar_seccion("GRAMATICA OPTIMIZADA (FACTORIZADA)")
    
    gram_optimizada = {
        "Stmt": [
            ["if", "(", "Cond", ")", "then", "Stmt", "OptElse"],
            ["a"]
        ],
        "Cond": [["x>0"]],
        "OptElse": [
            ["else", "Stmt"],
            ["ε"]
        ]
    }
    
    mostrar_gramatica("Gramatica factorizada", gram_optimizada)
    
    # ============================================================
    # EXPLICACION DEL FUNCIONAMIENTO
    # ============================================================
    mostrar_seccion("¿COMO FUNCIONA AHORA EL PARSER?")
    print("""
    Con la gramatica factorizada, el parser puede decidir DETERMINISTICAMENTE:
    
        Paso 1: Lee el prefijo comun 'if ( Cond ) then Stmt'
        Paso 2: Mira el siguiente token (lookahead):
                - Si el token es 'else' → aplica OptElse → else Stmt
                - Si NO hay 'else'      → aplica OptElse → ε (vacio)
    
    La decision ahora es CLARA y UNICA.
    """)
    
    # ============================================================
    # CONCLUSION
    # ============================================================
    mostrar_seccion("CONCLUSION")
    print("""
    La factorizacion por la izquierda es necesaria cuando:
        1. Dos o mas producciones comparten un prefijo comun
        2. Un parser LL(1) no puede decidir que regla aplicar
    
    La gramatica factorizada es EQUIVALENTE a la original
    pero es DETERMINISTICA y puede ser procesada por un parser predictivo.
    
    [OK] Demostracion completada.
    """)
    
    print("\n" + "=" * 70)
    print(" " * 22 + "FIN DE LA DEMOSTRACION")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()