def validar_expresion_pda(expresion):
    """
    Valida una expresion usando un automata de pila.
    Muestra paso a paso las operaciones SHIFT y REDUCE/POP.
    Retorna True si es valida, False si es invalida.
    """
    
    print("\n" + "-"*60)
    print("[PROCESANDO EXPRESION...]")
    print("-"*60)
    
    # Inicializar la pila (memoria LIFO)
    pila = []
    errores = []
    paso = 0
    
    # Recorrer la expresion caracter por caracter
    for caracter in expresion:
        paso += 1
        
        # OPERACION SHIFT: Guardar en pila (aperturas)
        if caracter in '([{':
            pila.append(caracter)
            print(f"Paso {paso:2d}: [SHIFT]  -> Guardar '{caracter}' en la pila")
            print(f"              Pila: {pila}")
        
        # OPERACION REDUCE/POP: Verificar cierre
        elif caracter in ')]}':
            if not pila:
                # Error: cierre sin apertura
                print(f"Paso {paso:2d}: [ERROR]  -> Cierre '{caracter}' pero la pila esta vacia")
                errores.append(f"Paso {paso}: Cierre '{caracter}' sin apertura previa")
                break
            
            # Obtener el tope de la pila (ultimo guardado)
            tope = pila[-1]
            
            # Verificar que el cierre coincida con la apertura
            if (caracter == ')' and tope == '(') or \
               (caracter == ']' and tope == '[') or \
               (caracter == '}' and tope == '{'):
                
                # OPERACION POP: Sacar de la pila
                pila.pop()
                print(f"Paso {paso:2d}: [REDUCE] -> Cierre '{caracter}' coincide con '{tope}'")
                print(f"              POP aplicado, pila: {pila}")
            else:
                # Error: no coinciden
                print(f"Paso {paso:2d}: [ERROR]  -> Cierre '{caracter}' no coincide con '{tope}'")
                errores.append(f"Paso {paso}: Se esperaba cerrar '{tope}' pero se encontro '{caracter}'")
                break
        
        # Ignorar otros caracteres (numeros, operadores, etc.)
        else:
            print(f"Paso {paso:2d}: [IGNORAR] -> '{caracter}' (no es parentesis)")
    
    # Verificar estado final de la pila
    print("\n" + "-"*60)
    print("[RESULTADO FINAL]")
    print("-"*60)
    
    if errores:
        # Hubo errores durante el procesamiento
        print("[INVALIDA] EXPRESION INVALIDA")
        print("   Motivos:")
        for error in errores:
            print(f"   * {error}")
        return False
    elif not pila:
        # Pila vacia = aceptacion por pila vacia
        print("[VALIDA] EXPRESION VALIDA")
        print("   * Todos los parentesis estan balanceados")
        print("   * La pila quedo vacia (aceptacion por pila vacia)")
        return True
    else:
        # Quedaron simbolos sin cerrar
        print("[INVALIDA] EXPRESION INVALIDA")
        print(f"   * Quedaron sin cerrar: {pila}")
        print(f"   * Faltaron {len(pila)} cierres")
        return False


# ============ PROGRAMA PRINCIPAL ============

def main():
    """
    Programa principal con menu de 2 opciones:
    1. Ingresar expresion
    2. Salir
    """
    
    print("\n" + "="*60)
    print(" AUTOMATA DE PILA - VALIDADOR DE EXPRESIONES")
    print("="*60)
    print("\n[DESCRIPCION]")
    print("  Este programa valida el balanceo de parentesis (),")
    print("  corchetes [] y llaves {} en una expresion.")
    print("  Simula el funcionamiento de un automata de pila")
    print("  mostrando las operaciones SHIFT y REDUCE/POP.")
    print("\n" + "="*60)
    
    contador = 1
    
    while True:
        # Mostrar menu
        print("\n" + "-"*60)
        print("[MENU PRINCIPAL]")
        print("  1. Ingresar una expresion para validar")
        print("  2. Salir")
        print("-"*60)
        
        opcion = input("\n[Opcion] (1 o 2): ").strip()
        
        # Opcion 1: Ingresar expresion
        if opcion == '1':
            print("\n" + "-"*60)
            print("[INGRESO DE EXPRESION]")
            print("-"*60)
            print("  * Usa parentesis (), corchetes [] o llaves {}")
            print("  * Ejemplo: {2 * [5 + (3 - 1)]}")
            print("  * Ejemplo: (2 + 3) * 4")
            print("  * Escribe 'volver' para regresar al menu")
            print("-"*60)
            
            while True:
                expresion = input(f"\n[Expresion #{contador}]: ").strip()
                
                # Opcion para volver al menu
                if expresion.lower() == 'volver':
                    break
                
                # Verificar que haya ingresado algo
                if not expresion:
                    print("[ERROR] Por favor ingresa una expresion valida.")
                    continue
                
                # Validar la expresion
                es_valida = validar_expresion_pda(expresion)
                
                # Mostrar resumen
                print("\n" + "-"*60)
                print("[RESUMEN]")
                print("-"*60)
                if es_valida:
                    print(f"  Expresion: {expresion}")
                    print("  Estado: VALIDA")
                else:
                    print(f"  Expresion: {expresion}")
                    print("  Estado: INVALIDA")
                print("-"*60)
                
                contador += 1
        
        # Opcion 2: Salir
        elif opcion == '2':
            print("\n" + "="*60)
            print(" [FIN] ¡Gracias por usar el validador!")
            print("="*60)
            break
        
        # Opcion invalida
        else:
            print("\n[ERROR] Opcion invalida. Elige 1 o 2.")


# ============ EJECUTAR PROGRAMA ============

if __name__ == "__main__":
    main()