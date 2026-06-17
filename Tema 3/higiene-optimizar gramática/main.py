# main.py
"""
PROGRAMA PRINCIPAL - DEMOSTRACION DE PATOLOGIAS DE GRAMATICAS
"""

import ambiguedad
import recursividad_iz
import factorizacion_iz

def main():
    print("\n" + "*" * 70)
    print(" " * 18 + "PATOLOGIAS DE GRAMATICAS")
    print(" " * 12 + "Demostraciones Teorico-Practicas")
    print("*" * 70)
    
    print("""
    Este programa demuestra tres patologias comunes en gramaticas formales:
    
    1. [AMBIGUEDAD] - Una misma cadena genera dos arboles diferentes
       (Demostracion INTERACTIVA - el usuario ingresa expresiones)
    
    2. [RECURSIVIDAD IZQUIERDA] - Defecto estructural que causa bucles infinitos
       (Demostracion del ALGORITMO)
    
    3. [FACTORIZACION IZQUIERDA] - Conflicto de decision del parser LL(1)
       (Demostracion de la GRAMATICA OPTIMIZADA)
    """)
    
    while True:
        print("\n" + "-" * 70)
        print("MENU PRINCIPAL")
        print("-" * 70)
        print("""
    1. [AMBIGUEDAD] - Probar expresiones matematicas
    2. [RECURSIVIDAD IZQUIERDA] - Ver algoritmo de eliminacion
    3. [FACTORIZACION IZQUIERDA] - Ver gramatica optimizada
    4. Salir
        """)
        
        opcion = input("Seleccione (1-4): ").strip()
        
        if opcion == '1':
            ambiguedad.main()
        elif opcion == '2':
            recursividad_iz.main()
        elif opcion == '3':
            factorizacion_iz.main()
        elif opcion == '4':
            print("\n" + "*" * 70)
            print(" " * 22 + "FIN DEL PROGRAMA")
            print("*" * 70 + "\n")
            break
        else:
            print("Opcion invalida. Intente nuevamente.\n")

if __name__ == "__main__":
    main()