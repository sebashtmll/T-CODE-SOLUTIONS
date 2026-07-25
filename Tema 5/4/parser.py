# pyrefly: ignore [missing-import]
import ply.yacc as yacc
from tokens import tokens

# Un documento puede ser una lista de elementos raíz o estar vacío
def p_document(p):
    '''document : element_list
                | empty'''
    p[0] = p[1] if p[1] is not None else {}

def p_element_list(p):
    '''element_list : element
                    | element_list element'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        # Fusionar diccionarios
        p[0] = p[1]
        p[0].update(p[2])

def p_element(p):
    '''element : key_or_services COLON VALUE NEWLINE
               | key_or_services COLON NEWLINE
               | key_or_services COLON NEWLINE INDENT block DEDENT'''
    if len(p) == 5:
        p[0] = {p[1]: p[3]}
    elif len(p) == 4:
        p[0] = {p[1]: None}
    else:
        p[0] = {p[1]: p[5]}

def p_key_or_services(p):
    '''key_or_services : KEY
                       | SERVICES'''
    p[0] = p[1]

# Un bloque es un conjunto de ítems de bloque (diccionarios o listas)
def p_block(p):
    '''block : block_item
             | block block_item'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        # Fusionar elementos del bloque
        p[0] = p[1]
        if isinstance(p[0], dict) and isinstance(p[2], dict):
            p[0].update(p[2])
        elif isinstance(p[0], list) and isinstance(p[2], list):
            p[0].extend(p[2])

def p_block_item(p):
    '''block_item : KEY COLON VALUE NEWLINE
                  | KEY COLON NEWLINE
                  | KEY COLON NEWLINE INDENT block DEDENT
                  | list_items'''
    if len(p) == 5:
        p[0] = {p[1]: p[3]}
    elif len(p) == 4:
        p[0] = {p[1]: None}
    elif len(p) == 7:
        p[0] = {p[1]: p[5]}
    else:
        p[0] = p[1]

# Una lista es una secuencia de elementos que empiezan por un guion '-'
def p_list_items(p):
    '''list_items : list_item
                  | list_items list_item'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_list_item(p):
    '''list_item : DASH VALUE NEWLINE'''
    p[0] = p[2]

def p_empty(p):
    '''empty :'''
    p[0] = None

# Manejo de errores sintácticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en el token: {p.type} ({repr(p.value)}) en la línea {p.lineno}")
    else:
        print("Error de sintaxis: Fin de archivo (EOF) inesperado")

# Construir el parser
parser = yacc.yacc()
