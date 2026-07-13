import re

# 1. Definicion de tokens especificos para Dockerfile
tokens = [
    ('INSTRUCTION', r'\b(FROM|RUN|CMD|COPY|ADD|ENV|WORKDIR|EXPOSE)\b'), # Instrucciones principales [cite: 124]
    ('COMMENT', r'#.*'),                                                # Comentarios [cite: 123]
    ('IP', r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'),                      # Formato IP (util si hay parámetros de red) [cite: 171]
    ('ARGUMENT', r'[a-zA-Z0-9_\-\/\.\:]+'),                              # Argumentos, rutas o valores [cite: 173]
    ('NEWLINE', r'\n'),                                                 # Salto de linea [cite: 175]
    ('SKIP', r'[ \t]+'),                                                # Espacios y tabulaciones [cite: 177]
    ('MISMATCH', r'.'),                                                 # Caracteres no reconocidos [cite: 182]
]

def lexer(input_text):
    # Unir todas las expresiones en un solo patron [cite: 187]
    token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in tokens)
    
    line_num = 1
    line_start = 0
    
    for mo in re.finditer(token_regex, input_text, re.MULTILINE):
        kind = mo.lastgroup
        value = mo.group(kind)
        
        if kind == 'NEWLINE':
            line_start = mo.end() # Actualiza el inicio de la linea para el cálculo de columna [cite: 201]
            line_num += 1
            continue
        elif kind == 'SKIP' or kind == 'COMMENT':
            continue # Ignorar elementos irrelevantes para el analisis [cite: 207]
        elif kind == 'MISMATCH':
            raise RuntimeError(f'Error lexico: {value!r} inesperado en linea {line_num}')  # [cite: 222]
        
        column = mo.start() - line_start
        yield kind, value, line_num, column # Retorna los datos del token [cite: 225]

# Ejemplo de uso
if __name__ == "__main__":
    dockerfile_content = """
    # Imagen base
    FROM ubuntu
    RUN apt-get update
    """
    for token in lexer(dockerfile_content):
        print(token)