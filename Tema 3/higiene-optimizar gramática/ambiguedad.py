# ambiguedad.py
"""
DEMOSTRACION INTERACTIVA DE GRAMATICA AMBIGUA
El usuario ingresa una expresion y se muestran dos arboles diferentes
"""

class Nodo:
    def __init__(self, valor, izquierdo=None, derecho=None):
        self.valor = valor
        self.izquierdo = izquierdo
        self.derecho = derecho
    
    def __str__(self, nivel=0):
        ret = "  " * nivel + str(self.valor) + "\n"
        if self.izquierdo:
            ret += self.izquierdo.__str__(nivel + 1)
        if self.derecho:
            ret += self.derecho.__str__(nivel + 1)
        return ret

def evaluar(nodo):
    if nodo.valor not in ['+', '-', '*', '/']:
        return int(nodo.valor)
    izq = evaluar(nodo.izquierdo)
    der = evaluar(nodo.derecho)
    if nodo.valor == '+': return izq + der
    if nodo.valor == '-': return izq - der
    if nodo.valor == '*': return izq * der
    if nodo.valor == '/': return izq // der

def construir_arbol_izquierda(tokens):
    """Asociatividad izquierda: (a op b) op c"""
    if len(tokens) == 1:
        return Nodo(tokens[0])
    actual = Nodo(tokens[1], Nodo(tokens[0]), Nodo(tokens[2]))
    for i in range(3, len(tokens), 2):
        actual = Nodo(tokens[i], actual, Nodo(tokens[i+1]))
    return actual

def construir_arbol_derecha(tokens):
    """Asociatividad derecha: a op (b op c)"""
    if len(tokens) == 1:
        return Nodo(tokens[0])
    actual = Nodo(tokens[-2], Nodo(tokens[-3]), Nodo(tokens[-1]))
    for i in range(len(tokens)-4, -1, -2):
        actual = Nodo(tokens[i], Nodo(tokens[i-1]), actual)
    return actual

def parsear_expresion(entrada):
    tokens = []
    i = 0
    while i < len(entrada):
        if entrada[i].isdigit():
            num = entrada[i]
            while i+1 < len(entrada) and entrada[i+1].isdigit():
                i += 1
                num += entrada[i]
            tokens.append(num)
        elif entrada[i] in '+-*/':
            tokens.append(entrada[i])
        i += 1
    return tokens

def main():
    print("=" * 70)
    print(" " * 18 + "GRAMATICA AMBIGUA")
    print("=" * 70)
    print("\nRegla: E -> E + E | E - E | E * E | E / E | numero")
    print("\n[INFORMACION] Esta gramatica ES AMBIGUA por diseno.")
    print("             Cualquier expresion puede generar dos arboles diferentes")
    print("             porque no define precedencia ni asociatividad.\n")
    
    while True:
        print("-" * 70)
        expresion = input("Ingrese una expresion (ej: 9-5+2) o 's' para salir: ").strip()
        
        if expresion.lower() == 's':
            break
        
        if not expresion:
            continue
        
        tokens = parsear_expresion(expresion)
        
        if len(tokens) < 3 or len(tokens) % 2 == 0:
            print("Formato invalido. Use algo como: 9-5+2\n")
            continue
        
        print(f"\nExpresion: {expresion}")
        print(f"Tokens: {tokens}\n")
        
        arbol_izq = construir_arbol_izquierda(tokens)
        arbol_der = construir_arbol_derecha(tokens)
        
        resultado_izq = evaluar(arbol_izq)
        resultado_der = evaluar(arbol_der)
        
        print("ARBOL 1 (Asociatividad izquierda):")
        print(arbol_izq)
        print(f"Resultado: {resultado_izq}")
        
        print("\nARBOL 2 (Asociatividad derecha):")
        print(arbol_der)
        print(f"Resultado: {resultado_der}")
        
        print("\n[DEMOSTRACION] Se generaron DOS arboles de derivacion diferentes")
        print("               para la MISMA cadena de entrada.")
        
        if resultado_izq != resultado_der:
            print(f"               Resultados diferentes: {resultado_izq} vs {resultado_der}")
        else:
            print(f"               En este caso, ambos arboles coinciden en {resultado_izq}")
            print("               pero la gramatica SIGUE siendo ambigua (ej: 9-5+2)")
        
        print("\n[CONCLUSION] La gramatica ES AMBIGUA. El compilador no puede")
        print("             decidir que arbol de derivacion usar.\n")
    
    print("\n" + "=" * 70)
    print(" " * 22 + "FIN")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()