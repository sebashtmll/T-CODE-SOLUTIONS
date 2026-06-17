import turtle

class ParserSintacticoDibujo:
    def __init__(self):
        # Mapeo semantico del alfabeto formal de la UNEG (Σ = {a, c, g, t})
        self.alfabeto = {'a', 'c', 'g', 't'}
        
    def inicializar_pluma(self, titulo):
        """Configura el entorno grafico de renderizado."""
        pantalla = turtle.Screen()
        pantalla.setup(750, 750)
        pantalla.bgcolor("#f4f6f9")
        pantalla.title(f"Parser Sintactico UNEG - {titulo}")
        
        pluma = turtle.Turtle()
        pluma.speed(4)
        pluma.pensize(3)
        pluma.shape("classic")
        pluma.color("#1e293b") # Color elegante pizarra
        return pluma, pantalla

    def procesar_cadena(self, cadena_adn, titulo_figura):
        """
        Actúa como el motor de ejecución semantica del compilador.
        Verifica lexicamente la cadena y ejecuta las acciones de dibujo.
        """
        pluma, pantalla = self.inicializar_pluma(titulo_figura)
        print(f"\n[Parser Log]: Analizando sintacticamente la estructura para: {titulo_figura}")
        print(f"[Cadena Terminal]: {cadena_adn}")
        
        # Simulacion del Analizador Lexico / Verificacion de Alfabeto
        for posicion, token in enumerate(cadena_adn):
            if token not in self.alfabeto:
                print(f" ERROR LEXICO: Simbolo invalido '{token}' en la posicion {posicion}.")
                pluma.color("red")
                return False
            
            # Ejecución Semántica Orientada por la Sintaxis
            if token == 'a':
                pluma.forward(60)    # Avanza y dibuja linea
            elif token == 'c':
                pluma.left(90)       # Esquina 90 grados  izquierda
            elif token == 'g':
                pluma.right(90)      # Giro/Bifurcacion derecha
            elif token == 't':
                pluma.penup()        # Sube el lapiz (salto de trazo)
                pluma.forward(40)
                pluma.pendown()      # Baja el lapiz
                
        print(" COMPILACIÓN Y RENDERIZADO EXITOSO.")
        pantalla.exitonclick()

# --- MÓDULO DE PRUEBAS AUTOMATIZADAS ---
if __name__ == "__main__":
    parser = ParserSintacticoDibujo()
    
    # -------------------------------------------------------------------------
    # CASO 1: CUADRADO ESTANDAR
    # Cadena derivada de: S -> C -> cacacacac
    # -------------------------------------------------------------------------
    cadena_cuadrado = "cacacacac" 
    # Nota: Tu archivo PDF define la estructura como 'cacacacac'.
    
    # -------------------------------------------------------------------------
    # CASO 2: ARBOL PEQUEÑO (Tallo y Hoja)
    # Cadena derivada de: S -> D -> ata
    # -------------------------------------------------------------------------
    cadena_arbol_pequeno = "ata" 
    
    # -------------------------------------------------------------------------
    # CASO 3: ARBOL CON RAMAS LATERALES 
    # Cadena derivada de: S -> D -> agttga
    # -------------------------------------------------------------------------
    cadena_arbol_ramas = "agttga" 
    
    # -------------------------------------------------------------------------
    # CASO 4: CUBO TRIDIMENSIONAL
    # Cadena derivada de: S -> B -> CgCgC -> acacacacgacacacacgacacacac
    # -------------------------------------------------------------------------
    cadena_cubo = "acacacacgacacacacgacacacac"

    # --- Menú interactivo de ejecución ---
    print("=" * 60)
    print("    PARSER SINTACTICO DE CADENAS DE DIBUJO (T-CODE SOLUTIONS)  ")
    print("=" * 60)
    print("1. Dibujar Cuadrado ('cacacacac')")
    print("2. Dibujar Arbol Pequeño ('ata')")
    print("3. Dibujar Arbol con Ramas Laterales ('agttga')")
    print("4. Dibujar Cubo Tridimensional ('acacacacgacacacacgacacacac')")
    print("=" * 60)
    
    opcion = input("Seleccione el arbol sintactico a renderizar (1-4): ")
    
    if opcion == "1":
        parser.procesar_cadena(cadena_cuadrado, "Cuadrado Estandar")
    elif opcion == "2":
        parser.procesar_cadena(cadena_arbol_pequeno, "Arbol Pequeño")
    elif opcion == "3":
        parser.procesar_cadena(cadena_arbol_ramas, "Arbol con Ramas Laterales")
    elif opcion == "4":
        parser.procesar_cadena(cadena_cubo, "Cubo  Tridimensional")
    else:
        print("Opción invalida. Saliendo del analizador.")