#!/usr/bin/env python3
"""
Autómata Finito Determinista (AFD) para reconocer movimientos básicos de ajedrez
en notación algebraica estándar (SAN), según el subconjunto definido en el Tema 3.
Subconjunto: [Pieza] [Desambiguación] [x] Destino
Donde:
  - Pieza: K, Q, R, B, N (opcional para peones)
  - Desambiguación: ancho (a-h) y/o largo (1-8)
  - Captura: x (opcional)
  - Destino: coordenada (a-h)(1-8) (obligatorio)
"""

class AFD_MovimientoAjedrez:
    """
    Autómata finito determinista para validar movimientos de ajedrez.
    Estados:
      q0: Inicio
      q1: Pieza leída
      q2: Desambiguación de ancho leída
      q3: Desambiguación de largo leída
      q4: Captura (x) leída
      q5: Primera parte del destino (letra) leída
      q6: Aceptación (destino completo)
      q_error: Error (transición no definida)
    """
    
    def __init__(self):
        # Conjunto de símbolos válidos
        self.piezas = {'K', 'Q', 'R', 'B', 'N'}
        self.ancho = set('abcdefgh')
        self.largo = set('12345678')
        self.captura = {'x'}
        
        # Estado inicial
        self.estado_actual = 'q0'
        
        # Tabla de transiciones (función delta)
        # Formato: (estado, símbolo) -> siguiente_estado
        self.transiciones = {
            # Desde q0
            ('q0', 'pieza'): 'q1',
            ('q0', 'ancho'): 'q5',
            # Desde q1
            ('q1', 'ancho'): 'q2',
            ('q1', 'largo'): 'q3',
            ('q1', 'captura'): 'q4',
            ('q1', 'ancho_destino'): 'q5',
            # Desde q2
            ('q2', 'largo'): 'q3',
            ('q2', 'captura'): 'q4',
            ('q2', 'ancho_destino'): 'q5',
            # Desde q3
            ('q3', 'captura'): 'q4',
            ('q3', 'ancho_destino'): 'q5',   # <--- CORREGIDO (antes era 'largo_destino')
            # Desde q4
            ('q4', 'ancho_destino'): 'q5',
            # Desde q5
            ('q5', 'largo_destino'): 'q6',
        }
        
        self.estado_aceptacion = 'q6'
    
    def clasificar_simbolo(self, char):
        """Clasifica un carácter según su tipo para la tabla de transiciones.
           Expresión Regular equivalente:
           ^([KQRBN])?([a-h])?([1-8])?(x)?([a-h][1-8])$
        """
        if char in self.piezas:
            return 'pieza'
        elif char in self.ancho:
            return 'ancho'
        elif char in self.largo:
            return 'largo'
        elif char in self.captura:
            return 'captura'
        else:
            return None
    
    def transicion(self, estado, simbolo_tipo):
        """Aplica la función de transición delta."""
        clave = (estado, simbolo_tipo)
        return self.transiciones.get(clave, 'q_error')
    
    def validar_movimiento(self, movimiento):
        """
        Valida una cadena de movimiento contra el AFD.
        Retorna True si es válido, False en caso contrario.
        """
        self.estado_actual = 'q0'
        
        if not movimiento:
            return False
        
        i = 0
        n = len(movimiento)
        
        while i < n:
            char = movimiento[i]
            simbolo_tipo = self.clasificar_simbolo(char)
            
            if simbolo_tipo is None:
                self.estado_actual = 'q_error'
                break
            
            # Manejo especial para ancho en contexto de destino
            if simbolo_tipo == 'ancho' and self.estado_actual in {'q1', 'q2', 'q3', 'q4'}:
                simbolo_tipo = 'ancho_destino'
            
            # Manejo especial para largo en contexto de destino (CORREGIDO)
            if simbolo_tipo == 'largo' and self.estado_actual == 'q5':
                simbolo_tipo = 'largo_destino'
            
            # Aplicar transición
            self.estado_actual = self.transicion(self.estado_actual, simbolo_tipo)
            
            if self.estado_actual == 'q_error':
                break
            
            i += 1
        
        return self.estado_actual == self.estado_aceptacion and i == n


# ==================== PRUEBAS ====================

def probar_movimientos():
    """Función de prueba con casos válidos e inválidos."""
    afd = AFD_MovimientoAjedrez()
    
    movimientos_validos = [
        "e4",      # Peón
        "Nf3",     # Caballo
        "Bxe5",    # Alfil captura
        "Qh5",     # Dama
        "R1a1",    # Torre con desambiguación de largo
        "Bxa6",    # Alfil captura
    ]
    
    movimientos_invalidos = [
        "",        # Vacío
        "e",       # Destino incompleto
        "N",       # Solo pieza
        "Nf",      # Destino incompleto
        "x",       # Solo captura
        "a9",      # Rango inválido
    ]
    
    print("=" * 50)
    print("VALIDANDO MOVIMIENTOS DE AJEDREZ (AFD)")
    print("=" * 50)
    
    print("\n--- Movimientos VÁLIDOS ---")
    for mov in movimientos_validos:
        resultado = afd.validar_movimiento(mov)
        print(f"  '{mov}': {'✅ Válido' if resultado else '❌ Inválido'}")
    
    print("\n--- Movimientos INVÁLIDOS ---")
    for mov in movimientos_invalidos:
        resultado = afd.validar_movimiento(mov)
        print(f"  '{mov}': {'✅ Válido' if resultado else '❌ Inválido'}")

if __name__ == "__main__":
    probar_movimientos()